"""This module contains example data for testing."""

from serlo.model import Email, PhoneNumber, Person, WorkingUnit, UnitType, \
                        UnitStatus, Tag

def generate_emails():
    """Returns examples of emails."""
    return [Email(address="hello@example.org", location="Home"),
            Email(address="some-string-with-ü", location="Work"),
            Email(address="", location="")]

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
            """<email-address><address /><location></location></email-address>"""]

def generate_phone_numbers():
    """Returns example phone numbers."""
    return [PhoneNumber(number="0123456789", location="Mobile"),
            PhoneNumber(number="+490", location="Work"),
            PhoneNumber(number="", location="")]

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
            """<phone-number><number /><location></location></phone-number>"""]

def generate_tags():
    """Returns example tags."""
    return [Tag(tag_id=23), Tag(tag_id=11), Tag(tag_id=5979171)]

def generate_tag_specs():
    """Return XML specifications of tags corresponding to the objects returned
    by `generate_tags()`."""
    return ["""<tag>
                   <id type="integer">23</id>
                   <name>Newsletter</name>
               </tag>""",
            """<tag>
                 <id type="integer">11</id>
                 <name>My Tag</name>
               </tag>""",
            """<tag>
                 <id type="integer">5979171</id>
               </tag>"""]

def generate_person_ids():
    """Returns person ids corresponding to objects returned by
    `generate_person()`."""
    return ["23", "42", "1"]

def generate_persons():
    """Returns example objects of Type `Person`."""
    email1, email2, email3 = generate_emails()
    phone1, phone2, phone3 = generate_phone_numbers()
    tag1, tag2, tag3 = generate_tags()

    person3 = Person(first_name="",
                     last_name="",
                     emails=[],
                     phone_numbers=[],
                     tags=[])
    person2 = Person(first_name="Yannick",
                     last_name="Müller",
                     emails=[email2, email3],
                     phone_numbers=[phone2, phone3],
                     mentor=person3,
                     tags=[tag2])
    person1 = Person(first_name="Markus",
                     last_name="Miller",
                     emails=[email1],
                     phone_numbers=[phone1],
                     mentor=person2,
                     tags=[tag1, tag2, tag3])

    return [person1, person2, person3]

def generate_person_specs():
    """Returns XML specifications of persons corresponding to the objects
    returned by `generate_persons()`."""
    email1, email2, email3 = generate_email_specs()
    phone1, phone2, phone3 = generate_phone_number_specs()
    tag1, tag2, tag3 = generate_tag_specs()
    id1, id2, id3 = generate_person_ids()

    return [f"""<person>
                 <author-id type="integer">129</author-id>
                 <background>Student</background>
                 <company-id type="integer">2744</company-id>
                 <created-at type="datetime">2017-06-12T15:07:32Z</created-at>
                 <first-name>Markus</first-name>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">{id1}</id>
                 <last-name>Miller</last-name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <title></title>
                 <updated-at type="datetime">2018-03-29T13:00:47Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <company-name>Hello e.V.</company-name>
                 <linkedin-url nil="true"></linkedin-url>
                 <tags type="array">
                   {tag1}
                   {tag2}
                   {tag3}
                 </tags>
                 <avatar_url>https://secure.highrisehq.com/av/eJ</avatar_url>
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
                 <id type="integer">{id2}</id>
                 <last-name>Müller</last-name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <title></title>
                 <updated-at type="datetime">2018-03-29T13:00:47Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <company-name>Hello e.V.</company-name>
                 <linkedin-url nil="true"></linkedin-url>
                 <avatar_url>https://secure.highrisehq.com/av/eJ</avatar_url>
                 <tags type="array">
                   {tag2}
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
                 <id type="integer">{id3}</id>
                 <last-name />
                 <owner-id type="integer" nil="true"></owner-id>
                 <title></title>
                 <updated-at type="datetime">2018-03-29T13:00:47Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <company-name>Hello e.V.</company-name>
                 <linkedin-url nil="true"></linkedin-url>
                 <avatar_url>https://secure.highrisehq.com/av/eJ</avatar_url>
                 <tags type="array">
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

def generate_people():
    """Returns a list of person lists for testing."""
    person1, person2, person3 = generate_persons()
    id1, id2, id3 = generate_person_ids()

    return [[(id1, person1), (id2, person2), (id3, person3)],
            [(id1, person1), (id2, person2)],
            []]

def generate_people_specs():
    """Returns XML specifications of people lists corresponding to the
    lists returned by `generate_people()`."""
    person1, person2, person3 = generate_person_specs()

    return [f"<people>{person1} {person2} {person3}</people>",
            f"<people>{person1} {person2}</people>",
            f"<people />"]

def generate_working_units():
    """Create working units for testing."""
    person1, person2, person3 = generate_persons()

    return [WorkingUnit(name="project1",
                        description="My description",
                        overview_document="overview_document",
                        storage_url="storage_url",
                        unit_type=UnitType.project,
                        status=UnitStatus.perfect,
                        person_responsible=person1,
                        participants=[person3]),
            WorkingUnit(name="",
                        description="",
                        overview_document="",
                        storage_url="",
                        unit_type=UnitType.project,
                        status=None,
                        person_responsible=person2,
                        participants=[]),
            WorkingUnit(name="Support Unit Master",
                        description="A cool unit.",
                        overview_document="http://example.org",
                        storage_url="https://example.com/url/",
                        unit_type=UnitType.support_unit,
                        status=UnitStatus.ok,
                        person_responsible=person1,
                        participants=[person2]),
            WorkingUnit(name="Another support unit",
                        description="Hello World",
                        overview_document="Hello Document",
                        storage_url="",
                        person_responsible=person3,
                        unit_type=UnitType.support_unit,
                        status=UnitStatus.problems,
                        participants=[person1, person2])]

def generate_working_unit_specs():
    """Create working units for testing."""
    person1, person2, person3 = generate_person_specs()
    id1, id2, id3 = generate_person_ids()

    return [f"""<deal>
                 <account-id type="integer">30</account-id>
                 <author-id type="integer">13</author-id>
                 <background>My description</background>
                 <category-id type="integer">6436430</category-id>
                 <created-at type="datetime">2018-02-19T14:22:51Z</created-at>
                 <currency>USD</currency>
                 <duration type="integer">1</duration>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">1</id>
                 <name>project1</name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <party-id type="integer">{id1}</party-id>
                 <price type="integer">0</price>
                 <price-type>fixed</price-type>
                 <responsible-party-id type="integer" nil="true">
                 </responsible-party-id>
                 <status>pending</status>
                 <status-changed-on type="datetime" nil="true">
                 </status-changed-on>
                 <updated-at type="datetime">2018-02-27T16:39:41Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <category>
                   <id type="integer">6436430</id>
                   <name>Project</name>
                 </category>
                 {person1}
                 <parties type="array">
                   {person3}
                 </parties>
                 <subject_datas type="array">
                  <subject_data>
                    <id type="integer">25</id>
                    <subject_field_id type="integer">1224123</subject_field_id>
                    <subject_field_label>Status</subject_field_label>
                    <value>we are ahead of our schedule</value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">148</id>
                    <subject_field_id type="integer">1224165</subject_field_id>
                    <subject_field_label>Link to Overview Document</subject_field_label>
                    <value>overview_document</value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">44</id>
                    <subject_field_id type="integer">1258882</subject_field_id>
                    <subject_field_label>Link to G-Drive Folder</subject_field_label>
                    <value>storage_url</value>
                  </subject_data>
                 </subject_datas>
                </deal>""",
            f"""<deal>
                 <account-id type="integer">30</account-id>
                 <author-id type="integer">13</author-id>
                 <background></background>
                 <category-id type="integer">6436430</category-id>
                 <created-at type="datetime">2018-02-19T14:22:51Z</created-at>
                 <currency>USD</currency>
                 <duration type="integer">1</duration>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">2</id>
                 <name></name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <party-id type="integer">{id2}</party-id>
                 <price type="integer">0</price>
                 <price-type>fixed</price-type>
                 <responsible-party-id type="integer" nil="true">
                 </responsible-party-id>
                 <status>pending</status>
                 <status-changed-on type="datetime" nil="true">
                 </status-changed-on>
                 <updated-at type="datetime">2018-02-27T16:39:41Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <category>
                   <id type="integer">6436430</id>
                   <name>Project</name>
                 </category>
                 {person2}
                 <parties type="array">
                 </parties>
                 <subject_datas type="array">
                  <subject_data>
                    <id type="integer">25</id>
                    <subject_field_id type="integer">1224123</subject_field_id>
                    <subject_field_label>Status</subject_field_label>
                    <value></value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">148</id>
                    <subject_field_id type="integer">1224165</subject_field_id>
                    <subject_field_label>Link to Overview Document</subject_field_label>
                    <value></value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">44</id>
                    <subject_field_id type="integer">1258882</subject_field_id>
                    <subject_field_label>Link to G-Drive Folder</subject_field_label>
                    <value></value>
                  </subject_data>
                 </subject_datas>
                </deal>""",
            f"""<deal>
                 <account-id type="integer">30</account-id>
                 <author-id type="integer">13</author-id>
                 <background>A cool unit.</background>
                 <category-id type="integer">4849968</category-id>
                 <created-at type="datetime">2018-02-19T14:22:51Z</created-at>
                 <currency>USD</currency>
                 <duration type="integer">1</duration>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">789</id>
                 <name>Support Unit Master</name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <party-id type="integer">{id1}</party-id>
                 <price type="integer">0</price>
                 <price-type>fixed</price-type>
                 <responsible-party-id type="integer" nil="true">
                 </responsible-party-id>
                 <status>pending</status>
                 <status-changed-on type="datetime" nil="true">
                 </status-changed-on>
                 <updated-at type="datetime">2018-02-27T16:39:41Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <category>
                   <id type="integer">4849968</id>
                   <name>Support Unit</name>
                 </category>
                 {person1}
                 <parties type="array">
                   {person2}
                 </parties>
                 <subject_datas type="array">
                  <subject_data>
                    <id type="integer">25</id>
                    <subject_field_id type="integer">1224123</subject_field_id>
                    <subject_field_label>Status</subject_field_label>
                    <value>we are in line with our schedule</value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">148</id>
                    <subject_field_id type="integer">1224165</subject_field_id>
                    <subject_field_label>Link to Overview Document</subject_field_label>
                    <value>http://example.org</value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">44</id>
                    <subject_field_id type="integer">1258882</subject_field_id>
                    <subject_field_label>Link to G-Drive Folder</subject_field_label>
                    <value>https://example.com/url/</value>
                  </subject_data>
                 </subject_datas>
                </deal>""",
            f"""<deal>
                 <account-id type="integer">30</account-id>
                 <author-id type="integer">13</author-id>
                 <background>Hello World</background>
                 <category-id type="integer">4849968</category-id>
                 <created-at type="datetime">2018-02-19T14:22:51Z</created-at>
                 <currency>USD</currency>
                 <duration type="integer">1</duration>
                 <group-id type="integer" nil="true"></group-id>
                 <id type="integer">789</id>
                 <name>Another support unit</name>
                 <owner-id type="integer" nil="true"></owner-id>
                 <party-id type="integer">{id3}</party-id>
                 <price type="integer">0</price>
                 <price-type>fixed</price-type>
                 <responsible-party-id type="integer" nil="true">
                 </responsible-party-id>
                 <status>pending</status>
                 <status-changed-on type="datetime" nil="true">
                 </status-changed-on>
                 <updated-at type="datetime">2018-02-27T16:39:41Z</updated-at>
                 <visible-to>Everyone</visible-to>
                 <category>
                   <id type="integer">4849968</id>
                   <name>Support Unit</name>
                 </category>
                 {person3}
                 <parties type="array">
                   {person1}
                   {person2}
                 </parties>
                 <subject_datas type="array">
                  <subject_data>
                    <id type="integer">25</id>
                    <subject_field_id type="integer">1224123</subject_field_id>
                    <subject_field_label>Status</subject_field_label>
                    <value>we are behind schedule</value>
                  </subject_data>
                  <subject_data>
                    <id type="integer">148</id>
                    <subject_field_id type="integer">1224165</subject_field_id>
                    <subject_field_label>Link to Overview Document</subject_field_label>
                    <value>Hello Document</value>
                  </subject_data>
                 </subject_datas>
                </deal>"""]

def generate_working_unit_list_spec():
    """Returns a spec containing all working_units defined by
    `generate_working_units()`."""
    unit1, unit2, unit3, unit4 = generate_working_unit_specs()

    return f"""<deals>
                {unit1}
                <deal><category-id type="integer">1</category-id></deal>
                <deal>
                  <category-id type="integer">4849968</category-id>
                  <status>lost</status>
                </deal>
                {unit2}
                {unit3}
                <deal><category-id type="integer">23</category-id></deal>
                <deal>
                  <category-id type="integer">4849968</category-id>
                  <status>won</status>
                </deal>
                {unit4}
                <deal><category-id type="integer">56775</category-id></deal>
               </deals>"""

def generate_mentoring_spec():
    """Retruns a spec specifing all mentoring relationships."""
    id2, id3 = generate_person_ids()[1:]
    person1, person2 = generate_person_specs()[:2]

    return f"""<deals>
                <deal>
                 <party-id type="integer">{id2}</party-id>
                 <category-id type="integer">6438903</category-id>
                 <parties type="array">
                   {person1}
                 </parties>
                </deal>
                <deal><category-id type="integer">23</category-id></deal>
                <deal><category-id type="integer">56775</category-id></deal>
                <deal>
                 <party-id type="integer">{id3}</party-id>
                 <category-id type="integer">6438903</category-id>
                 <parties type="array">
                   {person2}
                 </parties>
                </deal>
               </deals>"""
