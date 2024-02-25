Bard_PROMPT_TEMPLATE = '''Background:
In Android, XML configuration compatibility bugs occur when the processing of these XML configuration files in Android Apps is inconsistent across different Android API levels.

The processing of XML elements and attributes in XML configuration files is subject to change as the Android framework evolves, resulting in XML configuration compatibility bugs.

XML elements in a configuration file are generally processed by the Android framework in three steps: (1) parse XML elements in XML configuration files; (2) load parsed attribute values in XML elements to set the fields of corresponding UI objects; and (3) process loaded attribute values to render UI objects' behavior at runtime.

XML configuration compatibility bugs can arise if there are changes in the implementation of these three steps across Android API levels, resulting in different visual effects across Android API levels.

Bard Task:
Can the following XML elements and their attributes cause XML configuration compatibility bugs across Android API levels. Remember that different visual effects across Android API levels means that there exist XML configuration compatibility bugs, and XML configuration compatibility bugs can arise if there are changes in the implementation of above three steps across Android API levels. Only consider the conditions when Android API levels >= 21.
```xml
%s
```

Bard Response:
Answer me with either `[Yes]` or `[No]` at the first line, and give explanation. Where `[Yes]` represents that the given XML elements or the XML elements’ attributes can cause XML configuration compatibility bugs, and '[NO]' represents that the given XML elements or the XML elements' attributes cannot cause XML configuration compatibility bugs. If the answer is `[Yes]`, Bard should also give the complete issue-inducing XML elements and their corresponding issue-inducing attributes included in customized special-XML code blocks (```s-xml and ```) and customized special-attribute code blocks (```s-attr and ```), respectively.
'''

ChatGPT_PROMPT_TEMPLATE = '''Background:
In Android, XML configuration compatibility bugs occur when the processing of these XML configuration files in Android Apps is inconsistent across different Android API levels.

The processing of XML elements and attributes in XML configuration files is subject to change as the Android framework evolves, resulting in XML configuration compatibility bugs.

XML elements in a configuration file are generally processed by the Android framework in three steps: (1) parse XML elements in XML configuration files; (2) load parsed attribute values in XML elements to set the fields of corresponding UI objects; and (3) process loaded attribute values to render UI objects' behavior at runtime.

XML configuration compatibility bugs can arise if there are changes in the implementation of these three steps across Android API levels, resulting in different visual effects across Android API levels.

ChatGPT Task:
Can the following XML elements and their attributes cause XML configuration compatibility bugs across Android API levels. Remember that different visual effects across Android API levels means that there exist XML configuration compatibility bugs, and XML configuration compatibility bugs can arise if there are changes in the implementation of above three steps across Android API levels. Only consider the conditions when Android API levels >= 21.
```xml
%s
```

ChatGPT Response:
Answer me with either `[Yes]` or `[No]` at the first line, and give explanation. Where `[Yes]` represents that the given XML elements or the XML elements’ attributes can cause XML configuration compatibility bugs, and '[NO]' represents that the given XML elements or the XML elements' attributes cannot cause XML configuration compatibility bugs. If the answer is `[Yes]`, ChatGPT should also give the complete issue-inducing XML elements and their corresponding issue-inducing attributes included in customized special-XML code blocks (```s-xml and ```) and customized special-attribute code blocks (```s-attr and ```), respectively.
'''