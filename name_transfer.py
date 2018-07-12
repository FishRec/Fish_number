import os 
import xml.etree.ElementTree as ET


cwd='D:/program/mackerel/'#母資料夾
classes={'1','2','3'}  #需要更改的子資料夾
new_count = 0;#用來計算第幾張圖片
for index,name in enumerate(classes):#遍訪資料夾內部所有檔案
    class_path=cwd+name+'/'#組裝出子資料夾路徑
    new_str= 'ms'#新的名稱
    new_name =new_str+str(new_count);#新的名稱+編號
    for img_name in os.listdir(class_path): #走訪每個資料夾的檔案
        img_path=class_path+img_name #每一个图片的地址 
        
        if(".jpg" in img_name):#是圖片 
            old_name = img_name.split('.') #記錄舊的名子再來找excel檔案
            name_xml = old_name[0] +'.xml'

            if not os.path.exists(class_path+str(new_name)+'.jpg'):
                #改成目標圖片名稱(使用絕對位置)
                print(img_path+"圖片重新命名成功")
                os.rename(img_path , class_path+str(new_name)+'.jpg')

            if not os.path.exists(class_path+str(new_name)+'.xml'):
                #讀入xml
                Tree = ET.parse(class_path+name_xml)
                root = Tree.getroot()
                #更改屬性節點
                sub1 =  root.find('filename')
                sub1.text = new_name  
                sub2 = root.find("path")
                sub2.text = class_path+str(new_name)+'.jpg'

                
                #重新幫xml命名
                Tree.write(class_path+str(old_name[0])+'.xml')
                os.rename(class_path+str(old_name[0])+'.xml',class_path+str(new_name)+'.xml')
                print("XML重新命名成功")
                #改完xml更新檔案名稱
                new_count = new_count+1;
                new_name = new_str+str(new_count);
        