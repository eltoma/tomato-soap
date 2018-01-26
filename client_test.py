from zeep import Client

ip = '127.0.0.1'
port = 8000
client = Client("http://%s:%s/?wsdl" % (ip, port))
#print(client.wsdl.dump())

### say_hello_plus
factory = client.type_factory("ns0")
name = factory.Name(first_name='Kylin', last_name='Shu')
names = factory.NameArray([name, name])
r = client.service.say_hello_plus(names)
print(r)

### say_hello_plus
factory = client.type_factory("ns0")
names = factory.stringArray(["Kylin", "Shu"])
r = client.service.say_hello_plus2(names)
print(r)