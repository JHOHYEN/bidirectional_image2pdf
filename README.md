# bidirectional_image2pdf
Converts image files to PDF files, or PDF files to image files.


## Requirements
```
pip install -r requirements.txt
```
Besides, you need to install the followings: 
* python3 (tested on 3.8)

## Useage
This is the method for converting files (pdf, image) as desired by the user.
It converts image files to PDF files, or PDF files to individual image files.
Conversion from image files to PDF can be done either by creating a single file or by generating a PDF for each image.

### Convert image to PDF

1. Created as one PDF file
```
python image2pdf.py -to pdf -sum sum -r image_path -o save_path
```
2. Create a PDF file for each image
```
python image2pdf.py -to pdf -r image_path -o save_path
```


### Convert PDF to image

The PDF to image conversion process, you can change the '-img' option to jpg or png.

```
python image2pdf.py -to img -img jpg -r pdf_path -o save_path
python image2pdf.py -to img -img png -r pdf_path -o save_path
```
