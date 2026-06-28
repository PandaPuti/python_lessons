albums = {
    "Thriller": "1982-11-30",
    "Back in Black": "1980-07-25",
    "The Dark Side of the Moon": "1973-03-01",
    "The Bodyguard": "1992-11-17",
    "Rumours": "1977-02-04",
    "Saturday Night Fever": "1977-11-15",
    "Elton John - Greatest Hits": "1974-11-08",
    "Led Zeppelin IV": "1971-11-08",
    "Bad": "1987-08-31",
    "Jagged Little Pill": "1995-06-13",
    "Come On Over": "1997-11-04",
    "Sgt. Pepper's Lonely Hearts Club Band": "1967-05-26",
    "Falling into You": "1996-03-11",
    "Hotel California": "1976-12-08",
    "Dirty Dancing": "1987-08-21",
    "21": "2011-01-24",
    "Let's Talk About Love": "1997-11-14",
    "1": "2000-11-13",
    "Dangerous": "1991-11-26",
    "The Immaculate Collection": "1990-11-09"
}
len(albums)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum(numbers)

marks = [78, 90, 88.5, 60, 23, 45, 62, 100]
sorted_marks = sorted (marks)
sorted_marks #[23, 45, 60, 62, 78, 88.5, 90, 100]
marks #[78, 90, 88.5, 60, 23, 45, 62, 100]
marks.sort()
marks
[23, 45, 60, 62, 78, 88.5, 90, 100]

def add1(a):
    b = a + 1
    return b
c = add1(9)
c #10

def add1(a):
    """ add 1 to a"""
    b = a + 1
    return b
c = add1(9)
c
help(add1)
Help on function add1 in module __main__:

add1(a)
    add 1 to a

#function with no return

def MJ():
    print('Michael Jackson')
MJ()

#function with no body , write pass in the body ,python returns None if print the function call
def NoBody():
    pass
print(NoBody())
None

album_ratings = [10.0,8.5,9.5]
for i, s in enumerate(album_ratings):
    print("Album", i, "rating is", s)

#collecting arguments with *
def artistsName(*names):
  for name in names:
    print(name)
artistsName('Alka','Abhijeet','Sonu','Udit','Arijit')

Alka
Abhijeet
Sonu
Udit
Arijit

#this what happens , n number of arguments are collected in the tuple named names 
def artistsName(*names):
  print(names)
  for name in names:
    print(name)
artistsName('Alka','Abhijeet','Sonu','Udit','Arijit')
('Alka', 'Abhijeet', 'Sonu', 'Udit', 'Arijit')
Alka
Abhijeet
Sonu
Udit
Arijit
    
