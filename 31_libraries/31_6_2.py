import re

text = 'A578BE777 OP233787 K901BH666 CT46599 CNИ2929П777 666AMP666'
cars_pattern = r"[O,P,E,T,I,A,H,K,X,C,B,M]\d{3}[O,P,E,T,I,A,H,K,X,C,B,M]{2}\d{2,3}"
taxi_pattern = r"[O,P,E,T,I,A,H,K,X,C,B,M]{2}\d{5,6}"

cars = re.findall(cars_pattern, text)
print(cars)
taxi = re.findall(taxi_pattern, text)
print(taxi)
