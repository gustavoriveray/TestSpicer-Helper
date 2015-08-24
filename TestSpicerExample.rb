load "TestSpicerAPI.rb"

sessionId = start_test('CucumberRuby', 'Testing', 'example', 'This is an example', 'Something', 'None')

name = get_random_name(sessionId)['firstname']
lastname = get_random_name(sessionId)['lastname']
email = get_random_email(sessionId)['email']
age = get_random_age(sessionId, "28", "35" )['year']
areacode = get_random_phone(sessionId)['areacode']
phone = get_random_phone(sessionId)['number']
string = get_random_alphabet_string(sessionId, "10")['string']

postalcode = get_random_alphabet_string(sessionId, "5")['string']

puts name
puts lastname
puts email.downcase
puts age
puts areacode << " " << phone
puts string
puts postalcode

finish_test(sessionId)