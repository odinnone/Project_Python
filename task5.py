# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print('NOT(',x,'AND',y,'AND',z,')=',not x or not y or not z)