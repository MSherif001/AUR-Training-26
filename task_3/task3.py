from abc import ABC,abstractmethod
from enum import Enum

####### class declaration#######

class ItemStatus (Enum):
    
    AVAILABLE = 1
    CHECKED_OUT = 2
    LOST = 3

class Library_item(ABC):
    loan_period:int
    
    def __init__ (self,title,State):
            self.title = title
            self._state = State
    
    @abstractmethod
    def  get_state (self):
        ...
    
    @abstractmethod
    def checkout(self):
        if self._state == ItemStatus.AVAILABLE :
            self._state = ItemStatus.CHECKED_OUT
        
    @abstractmethod
    def return_item(self):
        self._state = ItemStatus.AVAILABLE
    
    @abstractmethod
    def mark_lost(self):
        self._state = ItemStatus.LOST
    
    @abstractmethod
    @classmethod
    def from_dict (cls):
        ...
    
    @abstractmethod
    def __lt__(self, other):
        return self.title < other.title
    
    @abstractmethod
    def __str__(self):
        return f"{self.title} ({self.__class__.__name__}) - {self._state.name}"
    
    @abstractmethod
    def __repr__(self):
        return f"<{self.__class__.__name__} title='{self.title}', status='{self._state.name}'>"

class Book(Library_item):
    loan_period = 21
    no_of_books = 0
    
    def __init__ (self,title,author,isbn,State):
        super().__init__(title,State)
        self._author = author
        self._isbn = isbn
        Book.no_of_books += 1
    
    def get_state(self):
        return self._state 
    
    def checkout(self):
        return super().checkout()
    
    def mark_lost(self):
        return super().mark_lost()
    
    def return_item(self) :
        return super().return_item()
    
    @classmethod
    def Books_number(cls):
        return cls.no_of_books
    
    @staticmethod
    def isbn_check(isbnn):
        check_isbn = isbnn.replace("-", "").replace(" ", "")
        if len(check_isbn) != 13 or not check_isbn.isdigit():
            return False
        total = 0
        for i in range(13):
            digit = int(check_isbn[i])
            if i % 2 == 0:
                total += digit * 1
            else:
                total += digit * 3 
        return total % 10 == 0
    
    @classmethod
    def from_dict(cls,dic:dict):#dictionary processing for the Book dictionary
        Title  = dic["title"]
        auth = dic["author"]
        isbnn = dic["isbn"]
        state = ItemStatus[dic["status"]]
        return cls(Title,auth,isbnn,state)


class DVD(Library_item):
    loan_period = 5
    no_of_DVDS = 0
    
    def __init__ (self,title,director,State):
        super().__init__(title,State)
        DVD.no_of_DVDS += 1
        self._director = director
    
    def get_state(self):
        return self._state 
    
    def checkout(self):
        return super().checkout()
    
    def mark_lost(self):
        return super().mark_lost()
    
    def return_item(self) :
        return super().return_item()
    
    @classmethod
    def DVDS_number(cls):
        return cls.no_of_DVDS
    
    @classmethod
    def from_dict(cls,dic):#dictionary processing for the dvd dictionary
        Title  = dic["title"]
        direct = dic["director"]
        state = ItemStatus[dic["status"]]
        return cls(Title,direct,state) 

class Magazine(Library_item):
    loan_period = 14
    no_of_Magazines = 0
    
    def __init__ (self,title,issue,State):
        super().__init__(title,State)
        Magazine.no_of_Magazines += 1
        self._issue = issue
    
    def get_state(self):
        return self._state 
    
    def checkout(self):
        return super().checkout()
    
    def mark_lost(self):
        return super().mark_lost()
    
    def return_item(self) :
        return super().return_item()
    
    @classmethod
    def Magazines_number(cls):
        return cls.no_of_Magazines
    
    @classmethod
    def from_dict(cls,dic):#dictionary processing for the dvd dictionary
        Title  = dic["title"]
        issue = dic["issue"]
        state = ItemStatus[dic["status"]]
        return cls(Title,issue,state)

####### End of class declaration #######

####### Data processing #######

class Database:
    def __init__(self, filename="database.txt"):
        self.filename = filename

    def load_items(self):
        ITEM_REGISTRY = {
            "Book": Book,
            "DVD": DVD,
            "Magazine": Magazine
        }
        
        raw_data = []
        processed_data = []
        
        try:
            with open(self.filename, "r") as f:
                for lines in f:
                    dicti = {}
                    line = lines.strip().split("|")
                    for items in line:
                        key, value = items.split("=")
                        dicti[key] = value
                    raw_data.append(dicti)
        except FileNotFoundError:
            print("Error while locating the file")

        for item in raw_data:
            item_type = item.pop("type", None)
            if item_type in ITEM_REGISTRY:
                ItemClass = ITEM_REGISTRY[item_type]
                new_item = ItemClass.from_dict(item)
                processed_data.append(new_item)
                
        return processed_data


class Library:
    def __init__(self, database: Database):
        self.db = database
        self.collection = self.db.load_items()

    def add_item(self, item):
        self.collection.append(item)

    def find_by_title(self, title):
        for item in self.collection:
            if item.title == title:
                return item
        print("Item not found")

    def checkout(self, title):
        item = self.find_by_title(title)
        if item:
            item.checkout()
        else:
            print("Item not found.")

    def list_available(self):
        for item in sorted(self.collection):
            if item.get_state() == ItemStatus.AVAILABLE:
                print(item)

# if __name__ == "__main__":
#     my_db = Database("database.txt")
    
#     alex_library = Library(my_db)
    
#     print("Available items in the library:")
#     alex_library.list_available()
####### End of processing data #######
