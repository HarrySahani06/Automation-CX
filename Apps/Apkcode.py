import os

class APK:
    absolute_path = ''
    def eleve_apk(self):
        self.absolute_path = os.path.dirname(__file__)+"/Eleve.apk"
        #print(absolute_path)
        return self.absolute_path
    def CX_apk(self,version):
        self.absolute_path = str(os.path.dirname(__file__)+"/"+version+".apk")
        #print(absolute_path)
        return self.absolute_path

# apk_object =APK()
# path=apk_object.CX_apk("1.31.10")
# print("path for apk is : " +path)

