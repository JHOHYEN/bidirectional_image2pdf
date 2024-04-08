##################################################
# This is a code that converts image files to    #
# PDF files, or PDF files to image files.        #
#                                                #
# Users can convert the entire set of files into #
# one single file, or generate individual        #
# PDF files for each file.                       #
#                                                #
# During the process of converting PDF files to  #
# images, conversion to JPG or PNG formats       #
# is possible.                                   #
# This is an update based on Github code.        #
##################################################

from PIL import Image
import os, sys
import argparse
from pdf2image import convert_from_path

class ImagetoPdf:
    def __init__(self, sum_flag, file_path, result_path):
        print('Start to convert')
        self.sum_flag = sum_flag
        self.file_path = file_path
        self.result_path = result_path
        self.validFormats = ('.jpg','.jpeg','.png','.JPG','.PNG')
        self.pictures = []
        self.files = os.listdir(self.file_path)
        self.convertPictures()
        sys.exit('Conversion is complete.')
             
    def filter(self, item):
        return item.endswith(self.validFormats)
       
    def clean(self, name):
        return ''.join(name.split('.')[:-1])
            
    def sortFiles(self):
        return sorted(self.files)
    
    def getPictures(self):
        pictures = list(filter(self.filter, self.sortFiles()))
        if self.isEmpty(pictures):
            sys.exit(" [Error] there are no pictrues in the directory ! ")
        print('pictures are : \n {}'.format(pictures))
        return pictures      
                    
    def isEmpty(self, items):
        return True if len(items) == 0 else False

    def convertPictures(self):
        if self.sum_flag == True:
            for picture in self.getPictures():
                self.pictures.append(Image.open(picture).convert('RGB'))
            self.save(picture)        

        elif self.sum_flag == False: 
            for picture in self.getPictures():
                self.pictures.append(Image.open(picture).convert('RGB'))
                self.save(self.clean(picture))
          
    def save(self, file_name):
        if self.sum_flag == True:
            self.pictures[0].save(f'{self.result_path}/combined.pdf', save_all=True, append_images=self.pictures[1:])
        else:
            self.pictures[0].save(f'{self.result_path}/{file_name}.pdf', save_all=True, append_images=self.pictures[1:])
    
class PdftoImage:
    def __init__(self, file_path, result_path):
        self.file_path = file_path
        self.result_path = result_path
        self.files = os.listdir(self.file_path)
        
        self.convertPdf()
        sys.exit('Conversion is complete.')
    
    def filter(self, item):
        return item.endswith('.pdf')
    
    def isEmpty(self, items):
        return True if len(items) == 0 else False
    
    def sortFiles(self):
        return sorted(self.files)
    
    def clean(self, name):
        return ''.join(name.split('.')[:-1])
    
    def convertPdf(self):
        file = list(filter(self.filter, self.sortFiles()))
        
        for name in file:
            file_name = self.file_path + '/' + name
            pages = convert_from_path(file_name, thread_count=4)
            for i, page in enumerate(pages):
                new_name = self.clean(name)
                if args.image_type =='jpg':
                    page.save(f"{self.file_path}/{new_name}_{str(i)}.jpg", 'JPEG')
                
                elif args.image_type =='png':
                    page.save(f"{self.file_path}/{new_name}_{str(i)}.png", 'PNG')


def run(args):    
    if args.change_type == 'pdf':
        if args.make_onefile == 'sum':
            sum_flag = True
        else:
            sum_flag = False
       
        ImagetoPdf(sum_flag, args.read_path, args.output_path)
        
    elif args.change_type == 'img':
        PdftoImage(args.read_path, args.output_path)
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-to", "--change_type", required=False, type=str, default='pdf',
                        help="want change type(pdf = image to pdf / img = pdf to image)")
    parser.add_argument("-img", "--image_type", required=False, type=str, default='jpg',
                        help="want image type(jpg or png type)")
    parser.add_argument("-sum", "--make_onefile", required=False, type=str, default='False', 
                        help="select save one file or individual files")
    parser.add_argument("-r", "--read_path", required=False, type=str, 
                        help="read path")
    parser.add_argument("-o", "--output_path", required=False, type=str,
                        help="output path")
    
    # Example: Convert image file to pdf file
    # 
    # python image2pdf.py -to pdf -sum sum -r image_path -o save_path
    #
    
    # Example: Convert pdf file to image file
    #
    # python image2pdf.py -to img -img jpg -r pdf_path -o save_path
    # 

    args = parser.parse_args()
    run(args)
