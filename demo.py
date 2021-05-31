# coding=utf-8

from nowatermark import WatermarkRemover

path = '../data/'

watermark_template_filename = path + 'mylogo.jpg'
remover = WatermarkRemover()
remover.load_watermark_template(watermark_template_filename)
remover.remove_watermark(path + 'watermarked_lung.jpg', path + 'watermarked_lung-result.jpg')