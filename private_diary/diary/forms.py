import os


from django import forms
from django.core.mail import EmailMessage


#
# 問い合わせフォーム
#   入力項目
#       ・お名前            1行文字入力、30文字
#       ・メールアドレス    メールアドレス入力
#       ・タイトル          1行文字入力、30文字
#       ・メッセージ        改行付き文字列
#
class InquiryForm(forms.Form):
    # 入力項目はクラス-フィールド変数として定義する
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)


    # コンストラクタでフィールドに対する詳細定義を行う
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # 各フォームフィールドエレメントにclass属性とplaceholder属性を設定する
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力して下さい'


        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力して下さい'


        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力して下さい'


        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力して下さい'


    # メールを送信するメソッドを定義する
    def send_mail(self):
        # 承認された入力データを取り出す
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']


        subject = f'お問い合わせ {title}'
        body = f'送信者名: {name}\nメールアドレス: {email}\nメッセージ: {message}\n'
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [from_email]
        cc_list = [email]
        bcc_list = []


        mail = EmailMessage(subject=subject,body=body,to=to_list,cc=cc_list,bcc=bcc_list)
        mail.send()

from .models import Diary

# 日記入力フォーム定義
class DiaryCreateForm(forms.ModelForm):
    # 入力フォームの下になるモデルと使用するフィールドを指定する
    class Meta:
        model = Diary
        fields = ('title','content','photo1','photo2','photo3',)
    
    # コンストラクタ
    #   self     今回生成されたインスタンス
    #   *args    タプルによる引数
    #   **kwargs ディクショナリによる引数
    def __init__(self, *args , ** kwargs):
        # スーパークラスのコンストラクタを呼ぶ
        # → HTMLの基本形が作られる
        super().__init__(*args,**kwargs)
        # 出来た入力エレメントにclass属性を割り当てる
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
