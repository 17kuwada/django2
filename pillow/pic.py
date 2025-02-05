# pillowライブラリを使う

# Image         画像データを取り扱う 
# ImageFilter   画像に対してレタッチを行う(ぼかし、シャープネス、エッジ検出などの加工)
# ImageEnhance  画像に対してレタッチを行う(コントラスト、鮮やかさ、明るさなどの調整)
# ImageDraw     画像データに描画する
from PIL import Image,ImageFilter,ImageDraw,ImageEnhance

# 画像ファイルを開いて作業を開始する
im = Image.open("e.png")
# アルファチャンネルを削除する
im_ = im.convert('RGB')

# 画像データを印刷する
#   画像ファイルのフォーマット、大きさ、色空間
print(im.format, im.size, im.mode)
# 楕円を描く
#   ドローイングツールで画像を開く
draw = ImageDraw.Draw(im)
#   ellipse(楕円)
draw.ellipse((0, 0, im.width, im.height), outline=(0, 0, 0),width=20)
# 線を引く
#   line ((左上x,左上y,右下x,右下y), fill=(R,G,B), width=線幅)
#       fill    塗りつぶし
#       width   線幅
draw.line((0,0,im.height,im.width),fill=(64,64,64),width=8)
#   line(((x1,y1),(x2,y2),(x3,y3),....) )
# draw.line(((100,100),(200,200),(100,200),(100,200)), outline=(255,0,0), width=8)
#   polygon(((x1,y1),(x2,y2),(x3,y3),....), fill=,outline=,width=)
#       fill    塗りつぶし, None:塗りつぶしなし
#       outline 枠線色
#       width   線幅
draw.polygon(((100,100),(200,200),(100,200),(100,200)), outline=(255,0,0), width=8)
# ImageFilterを使って画像をレタッチする
#       全て大文字のフィルタはパラメータがない
#       クラスフィルターはパラメータで効果を調整できる
im_blur = im.filter(ImageFilter.GaussianBlur(radius=10))
im_blur = im_blur.filter(ImageFilter.RankFilter(size=13,rank=7))    # RankFilter 小文字入り
# im_blur = im_blur.filter(ImageFilter.CONTOUR)                       # CONTOUR     大文字のみ
#   明るさを調整する
im_e = ImageEnhance.Brightness(im_blur)
im_e = im_e.enhance(1.5)

# モノクロ変換
#   .convert('L')
# サイズ変換
#   .resize((im.width//4,im.height//4))
#   ※元の4分の1に縮小  「//4」 整数値となるように切り捨てる
# gray = im.convert('L').resize((im.width//4,im.height//4))
gray =im_e.resize((im.width//2,im.height//2))
print(gray.format,gray.size, gray.mode)

# gray.show()
# 編集した画像を指定した形式で保存する
#   save(ファイル名,形式)
gray.save('gray.png','png')
#   拡張子をもとに形式を推測するので適切な拡張子が指定されていれば形式は省略可能
