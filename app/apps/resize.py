from PIL import Image

def resize(a, b):
    ori_img = Image.open(a)
    tem_img = Image.open(b)

    if int(ori_img.width) < int(ori_img.height):
        print('height is longer than width')
        resize_width = int(int(ori_img.width) *
                        (512 / int(ori_img.height)))
        resize_img = ori_img.resize((resize_width, 512))
        position_x = abs(int((512 - int(resize_img.width))/2))
        tem_img.paste(resize_img, (position_x, 0))
        com_img = tem_img

    if int(ori_img.height) < int(ori_img.width):
        print('width is longer than height')
        resize_height = int(int(ori_img.height) *
                            (512 / int(ori_img.width)))
        resize_img = ori_img.resize((512, resize_height))
        position_y = abs(int((512 - int(resize_img.height))))
        tem_img.paste(resize_img, (0, position_y))
        com_img = tem_img

    if int(ori_img.height) == 512 and int(ori_img.width) == 512:
        print('same')
        com_img = ori_img

    return com_img
    