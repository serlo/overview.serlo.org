"""This module contains example data for testing."""

from serlo.model import Email, PhoneNumber, Person

def generate_emails():
    """Returns examples of emails."""
    return [Email(address="hello@example.org"),
            Email(address="some-string-with-ü"),
            Email(address="")]

def generate_email_specs():
    """Returns XML specifications of emails corresponding to the results of
    `emails()`."""
    return ["""<email-address>
                <address>hello@example.org</address>
                <id type="integer">161561239</id>
                <location>Home</location>
               </email-address>""",
            """<email-address>
                <address>some-string-with-ü</address>
                <id type="integer">34567</id>
                <location>Work</location>
               </email-address>""",
            """<email-address><address /></email-address>"""]

def generate_phone_numbers():
    """Returns example phone numbers."""
    return [PhoneNumber(number="0123456789"),
            PhoneNumber(number="+490"),
            PhoneNumber(number="")]

def generate_phone_number_specs():
    """Returns XML specifications of phone number corresponding to the objects
    returned by `generate_phone_numbers()`."""
    return ["""<phone-number>
                <id type="integer">23144</id>
                <location>Mobile</location>
                <number>0123456789</number>
               </phone-number>""",
            """<phone-number>
                <id type="integer">0</id>
                <location>Work</location>
                <number>+490</number>
               </phone-number>""",
            """<phone-number><number /></phone-number>"""]

def generate_persons():
    """Returns example objects of Type `Person`."""
    email1, email2, email3 = generate_emails()
    phone1, phone2, phone3 = generate_phone_numbers()

    return [Person(first_name="Markus", last_name="Miller",
                   emails=[email1], phone_numbers=[phone1]),
            Person(first_name="Yannick", last_name="Müller",
                   emails=[email2, email3], phone_numbers=[phone2, phone3]),
            Person(first_name="", last_name="", emails=[], phone_numbers=[])]

def generate_person_specs():
    """Returns XML specifications of persons corresponding to the objects
    returned by `generate_persons()`."""
    email1, email2, email3 = generate_email_specs()
    phone1, phone2, phone3 = generate_phone_number_specs()

    return [f"""<person>
                 <author-id type="integer">129</author-id>
                 <background>Student</background>
                 <company-id type="integer">2744</company-id>
                 <created-at type="datetime">2017-06-12T15:07:32Z</created-at>
                 <first-name>Markus</first-name>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">28</id>
                 <last-name>Miller</last-name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <title></title>
                 <updated-at type="datetime">2018-03-29T13:00:47Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <company-name>Hello e.V.</company-name>
                 <linkedin-url nil="true"></linkedin-url>
                 <avatar_url>https://secure.highrisehq.com/av/eJ</avatar_url>
                 <tags type="array">
                   <tag>
                     <id type="integer">53</id>
                     <name>Newsletter</name>
                   </tag>
                 </tags>
                 <contact-data>
                   <instant-messengers type="array"/>
                   <twitter-accounts type="array"/>
                   <addresses type="array">
                     <address>
                       <city></city>
                       <country>Germany</country>
                       <id type="integer">14070</id>
                       <location>Home</location>
                       <state></state>
                       <street></street>
                       <zip></zip>
                     </address>
                   </addresses>
                   <phone-numbers type="array">
                     {phone1}
                   </phone-numbers>
                   <web-addresses type="array"/>
                   <email-addresses type="array">
                     {email1}
                   </email-addresses>
                 </contact-data>
                 <subject_datas type="array" />
                </person>""",
            f"""<person>
                 <author-id type="integer">129</author-id>
                 <background>Student</background>
                 <company-id type="integer">2744</company-id>
                 <created-at type="datetime">2017-06-12T15:07:32Z</created-at>
                 <first-name>Yannick</first-name>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">28</id>
                 <last-name>Müller</last-name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <title></title>
                 <updated-at type="datetime">2018-03-29T13:00:47Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <company-name>Hello e.V.</company-name>
                 <linkedin-url nil="true"></linkedin-url>
                 <avatar_url>https://secure.highrisehq.com/av/eJ</avatar_url>
                 <tags type="array">
                   <tag>
                     <id type="integer">53</id>
                     <name>Newsletter</name>
                   </tag>
                 </tags>
                 <contact-data>
                   <instant-messengers type="array"/>
                   <twitter-accounts type="array"/>
                   <addresses type="array">
                     <address>
                       <city></city>
                       <country>Germany</country>
                       <id type="integer">14070</id>
                       <location>Home</location>
                       <state></state>
                       <street></street>
                       <zip></zip>
                    </address>
                   </addresses>
                   <phone-numbers type="array">
                     {phone2}
                     {phone3}
                   </phone-numbers>
                   <web-addresses type="array"/>
                   <email-addresses type="array">
                     {email2}
                     {email3}
                   </email-addresses>
                 </contact-data>
                 <subject_datas type="array" />
                 </person>""",
            f"""<person>
                 <author-id type="integer">129</author-id>
                 <background>Student</background>
                 <company-id type="integer">2744</company-id>
                 <created-at type="datetime">2017-06-12T15:07:32Z</created-at>
                 <first-name></first-name>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">28</id>
                 <last-name />
                 <owner-id type="integer" nil="true"></owner-id>
                 <title></title>
                 <updated-at type="datetime">2018-03-29T13:00:47Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <company-name>Hello e.V.</company-name>
                 <linkedin-url nil="true"></linkedin-url>
                 <avatar_url>https://secure.highrisehq.com/av/eJ</avatar_url>
                 <tags type="array">
                  <tag>
                     <id type="integer">53</id>
                     <name>Newsletter</name>
                   </tag>
                 </tags>
                 <contact-data>
                   <instant-messengers type="array"/>
                   <twitter-accounts type="array"/>
                   <addresses type="array">
                     <address>
                      <city></city>
                       <country>Germany</country>
                       <id type="integer">14070</id>
                       <location>Home</location>
                       <state></state>
                       <street></street>
                       <zip></zip>
                    </address>
                   </addresses>
                   <phone-numbers type="array">
                   </phone-numbers>
                   <web-addresses type="array"/>
                   <email-addresses type="array">
                   </email-addresses>
                 </contact-data>
                 <subject_datas type="array" />
                </person>"""]
