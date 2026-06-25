import pytesseract
import cv2
from tkinter import Tk,filedialog
Tk().withdraw()
image_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
)
import shutil
if shutil.which("tesseract") is None:
    print("Error: Tesseract is not installed or not in PATH")
else:
    print("Tesseract found at:", shutil.which("tesseract"))
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    print("Connection was succesful")
    image=cv2.imread(image_path)
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(img))
    # cv2.imshow("OUT PUT",cv2.resize(image,(800,600)))
    text=pytesseract.image_to_boxes(img)
    print(text)
    hig,wid,o=img.shape
    for i in text.splitlines():
        print(i)
        i=i.split(' ')
        print(i)
        h,w,hi,wi=int(i[1]),int(i[2]),int(i[3]),int(i[4])
        cv2.rectangle(img,(h,hig-w),(hi,hig-wi),(0,255,0),2)
    resized_img = cv2.resize(img, (800, 600))
    cv2.imshow("OUTPUT", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
