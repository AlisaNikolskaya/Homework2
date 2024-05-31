number_of_completed_homeworks=12
number_of_hours_spent=1.5
сourse_name='Python'
time_for_one_homework=number_of_hours_spent/number_of_completed_homeworks
print('Курс:',сourse_name,',', 'всего задач:', number_of_completed_homeworks,',', 'затрачено часов:', number_of_hours_spent,',', 'среднее время выполнения:', time_for_one_homework)

#вариант 2
number_of_completed_homeworks=12
number_of_hours_spent=1.5
сourse_name='Python'
time_for_one_homework=float(number_of_hours_spent/number_of_completed_homeworks)
print('Курс: ' + str(сourse_name) + ', ' + 'всего задач: ' + str(number_of_completed_homeworks) + ', ' + 'затрачено часов: ' + str(number_of_hours_spent) + ', ' + 'среднее время выполнения: ' + str(time_for_one_homework))
