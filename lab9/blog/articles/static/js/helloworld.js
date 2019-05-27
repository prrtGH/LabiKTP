var groupmates = [
{
"name": "Василий",
"group": "912-2",
"age": 19,
"marks": [4, 3, 5, 5, 4]
},
{
"name": "Анна",
"group": "912-1",
"age": 18,
"marks": [3, 2, 3, 4, 3]
},
{
"name": "Георгий",
"group": "912-2",
"age": 19,
"marks": [3, 5, 4, 3, 5]
},
{
"name": "Валентина",
"group": "912-1",
"age": 18,
"marks": [5, 5, 5, 4, 5]
}
];

var rpad = function(str, length) {
// js не поддерживает добавление нужного количества символов
// справа от строки то есть аналога ljust из языка Python здесь нет
str = str.toString(); // преобразование в строку
while (str.length < length)
str = str + ' '; // добавление пробела в конец строки
return str; // когда все пробелы добавлены, возвратить строку
};
var printStudents = function(students){
console.log(
rpad("Имя студента", 15),
rpad("Группа", 8),
rpad("Возраст", 8),
rpad("Оценки", 20)
);
// был выведен заголовок таблицы
for (var i = 0; i<=students.length-1; i++){
// в цикле выводится каждый экземпляр студента
console.log(
rpad(students[i]['name'], 15),
rpad(students[i]['group'], 8),
rpad(students[i]['age'], 8),
rpad(students[i]['marks'], 20)
);
}
console.log('\n'); // добавляется пустая строка в конце вывода
};
printStudents(groupmates);



var filterSt = function (students, groupNumber) { 
	for (var i in students) { 
		if(students[i]['group']==groupNumber){ 
			console.log( 
			rpad(students[i]['name'], 15), 
			rpad(students[i]['group'], 8), 
			rpad(students[i]['age'], 8), 
			rpad(students[i]['marks'], 20) 
			); 
		} 
	} 
} 

filterSt(groupmates, "912-2");