import xml.etree.ElementTree as ET

mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
print(myroot.tag)
# print(myroot[4].tag)


forecast = myroot[4]
print(forecast)

# time_1 = forecast[1]

# print (time_1)

# temperature = time_1[4]

# print(temperature.attrib)

# attribs = temperature.attrib

# for x in attribs.findall('value'):
first_three_forecast = forecast[:3]
print(first_three_forecast)
# for x in first_three_forecast:

time_1 = first_three_forecast[0]
print(time_1)
print(time_1[4].attrib)
temp_dic = time_1[4].attrib
print(temp_dic['value'])

time_2 = first_three_forecast[2]
print(time_1)

time_3 = first_three_forecast[2]
print(time_3)







