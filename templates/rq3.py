Bard_PROMPT_TEMPLATE = '''
Background:
In Android, XML configuration compatibility bugs occur when the processing of these XML configuration files in Android Apps is inconsistent across different Android API levels.

The processing of XML elements and attributes in XML configuration files is subject to change as the Android framework evolves, resulting in XML configuration compatibility bugs.

XML elements in a configuration file are generally processed by the Android framework in three steps: (1) parse XML elements in XML configuration files; (2) load parsed attribute values in XML elements to set the fields of corresponding UI objects; and (3) process loaded attribute values to render UI objects' behavior at runtime.

XML configuration compatibility bugs can arise if there are changes in the implementation of these three steps across Android API levels, resulting in different visual effect across Android API levels.

Bard Task:
The following XML elements and issue-inducing attribute `%s` can cause XML configuration compatibility bugs between Android API levels %d and %d (only consider these two Android API levels). The task is to repair the XML compatibility bugs. Bard needs to obey six rules when repairing: (1) attempt to repair the XML compatibility bugs by modifying the issue-inducing attributes or their values as less as possible. The modifying approaches include (a) specify issue-fixing attributes in the following issue-inducing XML elements to eliminate the inconsistent runtime behavior, (b) directly change the values of issue-inducing attributes, and (c) directly remove issue-inducing attributes; (2) If (1) is inapplicable for repairing, then specify other different types of XML elements to replace the following issue-inducing elements; (3) ensure the repairing changes to XML elements are minimized as much as possible; (4) do not introduce Android API calls or create new resource files or folders in the repaired results; (5) the visual effects of the repaired app are consistent between Android API levels %d and %d; and (6) the most importantly, the visual effects of the repaired app should be as similar as possible to the original app before repairing on Android API level %d.
```xml
%s
```

Bard Response:
The complete repaired result should be included in one XML code block (```xml and ```). Bard should give repairing explanation.
'''

ChatGPT_PROMPT_TEMPLATE = '''
Background:
In Android, XML configuration compatibility bugs occur when the processing of these XML configuration files in Android Apps is inconsistent across different Android API levels.

The processing of XML elements and attributes in XML configuration files is subject to change as the Android framework evolves, resulting in XML configuration compatibility bugs.

XML elements in a configuration file are generally processed by the Android framework in three steps: (1) parse XML elements in XML configuration files; (2) load parsed attribute values in XML elements to set the fields of corresponding UI objects; and (3) process loaded attribute values to render UI objects' behavior at runtime.

XML configuration compatibility bugs can arise if there are changes in the implementation of these three steps across Android API levels, resulting in different visual effect across Android API levels.

ChatGPT Task:
The following XML elements and issue-inducing attribute `%s` can cause XML configuration compatibility bugs between Android API levels %d and %d (only consider these two Android API levels). The task is to repair the XML compatibility bugs. ChatGPT needs to obey six rules when repairing: (1) attempt to repair the XML compatibility bugs by modifying the issue-inducing attributes or their values as less as possible. The modifying approaches include (a) specify issue-fixing attributes in the following issue-inducing XML elements to eliminate the inconsistent runtime behavior, (b) directly change the values of issue-inducing attributes, and (c) directly remove issue-inducing attributes; (2) If (1) is inapplicable for repairing, then specify other different types of XML elements to replace the following issue-inducing elements; (3) ensure the repairing changes to XML elements are minimized as much as possible; (4) do not introduce Android API calls or create new resource files or folders in the repaired results; (5) the visual effects of the repaired app are consistent between Android API levels %d and %d; and (6) the most importantly, the visual effects of the repaired app should be as similar as possible to the original app before repairing on Android API level %d.
```xml
%s
```

ChatGPT Response:
The complete repaired result should be included in one XML code block (```xml and ```). ChatGPT should give repairing explanation.
'''