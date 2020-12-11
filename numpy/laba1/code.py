import numpy as np
from PIL import Image

# считаем картинку в numpy array
img = Image.open(input())
data = np.array(img)

minOfPic = data.min()
maxOfPic = data.max()
updated_data = np.around((data - minOfPic * np.ones(data.shape)) * 255 / (maxOfPic - minOfPic))

# запись картинки после обработки
res_img = Image.fromarray(updated_data.astype('uint8'), 'L')
res_img.show()
res_img.save('Picture3_updated.png')





