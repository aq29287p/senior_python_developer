from math import perm

class Phone:
    
    #constructor
    def __init__(self, brand, price, camera_count, screen_size):
        self.brand = brand
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size
    #pure virtual method
    @classmethod
    def special_freature(cls):
        print("This is a special feature")

class Google_phone(Phone):
    #constructor with default values
    def __init__(self, brand='Google', price= 10, camera_count= 3, screen_size= 5):
        super().__init__(brand , price, camera_count, screen_size)
    #overriding the special feature method
    @classmethod
    def special_freature(cls, list_of_features):
        return sorted([ _i  for _i in list_of_features if _i > 10 and _i%2 == 0  ], reverse=True)

class Taiwan_phone(Phone):
    #constructor with default values
    def __init__(self, brand= 'Taiwan', price= 20, camera_count= 1, screen_size= 3):
        super().__init__(brand , price, camera_count, screen_size)
    
    #fibonacci series
    @classmethod
    def f_series(cls,int_of_features):
        a, b = 0, 1
        for i in range(int_of_features):
            a, b = b, a+b
        return a
        
    #overriding the special feature method
    @classmethod
    def special_freature(cls, int_of_features):
        f_number=str(cls.f_series(int_of_features))
        return perm(int(f_number[-2]), int(f_number[-1]))

