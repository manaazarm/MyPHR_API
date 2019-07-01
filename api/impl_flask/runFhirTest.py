# Import the relevant classes from fhir.model
from fhir.model import Patient, HumanName, Identifier, CodeableConcept, Coding, uri

# Create a new Patient object. Resource attributes can be passed in the constructor. Note
# that 'id' is the logical id of the Resource and has no relation to the Medical Record 
# Number (MRN)
p = Patient(id='patient1')                                  

# Give the patient an MRN
identifier = Identifier(
    type=CodeableConcept(coding=[Coding(system="http://hl7.org/fhir/v2/0203", code="MR")]),
    system='urn:oid:1.2.36.146.595.217.0.1',
    value='123456789'
)

# Lists can be assigned to attributes. 
# Alternatively p.identifier.append(identifier) could have been used.
p.identifier = [identifier]

# Native python values are automatically coerced to FHIR classes
p.active = True
name = HumanName()
name.use = 'official'
name.given = ['Melle', 'Sjoerd']
#name.family = ['Sieswerda']
p.name = [name]
# output: <class 'fhir.model._boolean.boolean'>

# Serialize to JSON and print the result. To serialize to XML use 'p.toXML()'.
print(p.dumps('json'))

