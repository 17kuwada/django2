from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import InquiryForm

# お問い合わせ送信内容をログに残す
import logging
logger = logging.getLogger(__name__)

# 'アプリ名:url名'からURLを取り出す

# ページ間でメッセージを送る機能

# Create your views here.
# ここにクラスを登録することによりアプリ内の画面を登録する

#   IndexViewクラスはindex.htmlを元にページを構成する

class IndexView(TemplateView):
    template_name = 'index.html'

# お問い合わせページ
class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('diary:index')


    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'メッセージを送信しました')
        messages.success(self.request, 'CCでメールを同報しています')
        messages.success(self.request, 'ご確認下さいませ')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
    

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
from django.core.paginator import Page

# 日記一覧
# ログインが必要で尚且つ一覧表示するViewを継承する
class DiaryListView(LoginRequiredMixin,generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by=2

    # 問い合わせ条件を設定する
    # ※今回は全行ではなくログインしている人の日記のみが対象となる
    def get_queryset(self):
        # Diaryテーブルから条件に当てはまる行を抽出する
        diaries = Diary.objects.filter(user=self.request.user).order_by('create_at')
        return diaries
        # return super().get_queryset()

# 日記を1件表示するビュー
#   DetailViewではpk変数で主キーを受け取る

class DiaryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'
# pk_url_kwarg='id'

from .forms import DiaryCreateForm
class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    # 登録成功時に表示するページのURL
    success_url = reverse_lazy('diary:diary_list')

    # 登録成功時の処理
    def form_valid (self,form):
        diary = form.save(commit=False)
        # 入力したユーザ情報を保存データに付与する
        diary.user = self.request.user
        # データを保存する
        diary.save()

        # すべて完了したのでテンプレートに送るメッセージをセットする
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)
    
    # 何かの問題で登録が出来なかった場合の処理
    def form_invalid(self, form):
        messages.success(self.request,'日記の作成に失敗しました')
        return super().form_invalid(form)
    
# 既存の日記を編集するビュー
# フォームは新規登録と同じ「DiaryCreateForm」を使用する
# LoginRequiredMixin を継承することによりログインを必要とするビューとなる
# generic.UpdateView を継承することにより既存データを編集するビューとなる
class DiaryUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm
    
    # 更新成功後処理
    #   成功した後に表示するページのURLを返す
    def get_success_url(self):
        # 日記詳細ページを開く。この時IDを指定して元々リンクしてきたデータのページを開く
        return reverse_lazy('diary:diary_detail',kwargs={'pk':self.kwargs['pk']})
    
    # 更新成功時の処理
    def form_valid(self, form):
        messages.success(self.request,'日記を更新しました。')
        return super().form_valid(form)
    
    # 更新失敗時の処理
    def form_invalid(self, form):
        messages.error(self.request,'日記の更新に失敗しました。')
        return super().form_invalid(form)
    
# 日記を削除するビュー
class DiaryDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,'日記を削除しました')
        return super().delete(request, *args, **kwargs)