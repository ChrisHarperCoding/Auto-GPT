## USER
I would like to mock up the following in a dashboard, what could the dashboard look like please?

**Overview**
_In reference to the attached email_
Document Archiver is a critical tool within the technical estate, which is primarily responsible for the movement of various client related documents between systems. The tool was developed in-house and is supported by the Application Support and Application Development teams.

_Examples of what the tool does_
-Movement of critical client documents from Symphony to Client Archive & XPLAN/Portal, e.g. Contract Notes
-Movement of other client document types, e.g. Cash advices; change of address letters
-Managing client account opening documents & storing them in the Client Archive
-Movement & archiving of valuation & tax packs, as submitted by client user groups within the business.
-Various other processes 

_Issues caused by problems with this process_
-Document Archiver fails due to a 'bad' file
-Document Archiver doesn't run at expected times
-Document Archiver issues which may not be recoverable to meet deadlines
-Failures not detected early enough
-High business volumes which exceed capacity of the system
-P1/P2 issue which cannot be resolved
-Knock-on incidents due to staff involvement / time spent on issues in this process, this can lead up to COO involvement at minimum in event of L4 escalation
-Unrecoverable failures resulting in critical contract notes not being available online in order to meet deadlines
-Visibility all the way to COO in event of L4 escalation (detailed in attached email)

_Request from Application Support_
-Discussion on automation of checks in order to alert automatically in the event of any issue that would cause a problem with the Document Archiver

-Automate checks?
  -SolarWinds?
  -ControlM?

_Current Solution_
-Relies primarily on manual checks and memorisation of this process or referral to documentation, which is extensive as this is a complicated process

-3x daily manual checks in the Application Support Checklist
-Details of current 'minimum' checks attached

_To Discuss_
-Automate checks
            -SolarWinds?
            -ControlM?

-Review the process
-Hourly runs of archiver? 
-Can we poll for files being present / investigate other solutions rather than having a scheduled task that only runs once per hour? And then another wait for SFTP
  -Files are sitting waiting to be processed for extended periods of time which can cause further issues in the event of a problem with the process that causes a backlog

-End result required 
  -Evidence that any files expected to have loaded into XPLAN within x period of time have loaded

Files in these locations should be processed within x minutes and should be visible in XPLAN within x minutes after entering these respective folders:
  \\svr-cpamlon-dc\workgrp\shared\temporary filing archive
  \\ukcloseam\data\Workgroups\Documents Filing\Invalid Files
  \\ukcloseam\data\Workgroups\Documents Filing
  \\ukcloseam\data\Departments\ITAppsLondon\LIVE\IT User Apps\IT Filing Archive
  \\ukcloseam\data\Workgroups\SIPP Documents Filing
  \\ldnxplanora01\pwc\PWC_POST_TRADE_REPORT\DOCUMENT_REPOSITORY

Alerting for any issues at any stage in the process

Detailed documentation on resolution to issues

Need specific SLA’s for each step of the process so that we can build alerting/monitoring/documentation based on this

How long is each step expected to take, what's the warning threshold for an alert, what's the critical threshold for an alert

_Satisfy KK's Checks that Archiver is Working as Expected_
Ideally we need the ability to track both processes - the Document Archiver process in general & tracking high priority items (Contract Notes process)

**11:00 am or 15:00 – The contract note process should start – If not started , an automatic notification to business asking why it hasn’t started . **

**Once the process has started , I need one notification to business and app support that all is fine . If it is not fine, then where is the problem prompting the team to investigate. **

  -We need the ability to see whether the Trade Settlements Team have started the morning contract note run at 11:00

To check the Document Archiver process in general:
-Produce a summary email as and when required to give a status update on Document Archiver if required (*This could also include status of Contract Notes unless it's best to have a separate email*)
-Regular scheduled emails on a periodic basis on a frequency that KK has requested ("11:00 am or 15:00 – The contract note process should start – If not started , an automatic notification to business asking why it hasn’t started. Once the process has started , I need one notification to business and app support that all is fine . If it is not fine, then where is the problem prompting the team to investigate") to give a status update on Document Archiver (*This will also include status of Contract Notes unless it's best to have a separate email*)

-Have a dashboard that states if the Document Archiver and Contract Notes are 'OK', 'Warning' or 'Critical' (*Separate status for each*). 
  At the moment, to give an update on the status of Document Archiver, involves lots of manual checks that takes a long period of time to give a definitive answer. We would like to be able to give an answer as and when required for the status of this process

Following details should be available so that any issues can be investigated:
Status of contract note runs (*Time Started, Time Finished*)
List of filenames picked up by the Document Archiver
  Flag any files with issues (*bad characters etc. Status above should update as any issues are rectified*)
Folder that the file was picked up from (*From the list of known locations as described above*)
Time started processing
Time ended processing (*Flag as an issue to be investigated if x file is not processed within agreed x Time Period*)
What stage the file processing is up to e.g
  Produced in Symphony
  Document Archiver started processing
  Document Archiver finished processing
  SFTP job ready to start
  SFTP job started
  SFTP job finished
  IRESS Doc Agent processing file (*if we can get this info*)
  Available in XPLAN? (*Yes / No*)

## ASSISTANT
Based on your requirements, I propose a dashboard that provides a comprehensive view of the Document Archiver's status and performance. This dashboard will have several sections, each focusing on different aspects of the tool, such as automation checks, process monitoring, and alerting. 

Here's a mockup of what the dashboard could look like:

**Dashboard Title: Document Archiver Monitoring and Performance**

1. **Automation Checks**
   - SolarWinds Status: OK / Warning / Critical
   - ControlM Status: OK / Warning / Critical

2. **Process Monitoring**
   - Document Archiver Status: OK / Warning / Critical
   - Contract Notes Status: OK / Warning / Critical
   - Hourly Runs of Archiver: Enabled / Disabled
   - Time Since Last Archiver Run: XX minutes ago
   - Files Pending Processing: XX

3. **Alerts and Notifications**
   - Unprocessed Files Alert Threshold: XX minutes
   - Contract Notes Alert Threshold: XX minutes
   - Current Alert Level: OK / Warning / Critical
   - Latest Alerts: (List of recent alerts with timestamps)

4. **Process Details**
   - Recent Contract Note Runs: (List of recent runs with start and end times)
   - Recent File Transfers: (List of filenames, source folder, start and end times)
   - Files with Issues: (List of filenames with problems, such as bad characters)
   - Processing Stage for Selected File: (Dropdown to select a file, display processing stage)
   - File Availability in XPLAN: Yes / No

5. **SLA Monitoring**
   - Time per Step: (List of steps with expected time, warning threshold, and critical threshold)
   - Current SLA Compliance: OK / Warning / Critical

6. **Summary Emails**
   - Last Document Archiver Status Email: (Timestamp and recipient list)
   - Last Contract Notes Status Email: (Timestamp and recipient list)

This dashboard layout should provide a comprehensive view of the Document Archiver tool's performance, making it easy to monitor and identify any issues. It allows for quick access to critical information and helps streamline the process of providing status updates to stakeholders. The dashboard can be customized further to include any additional metrics or visualizations that may be required.

## USER
Thank you that's great. I have access to SolarWinds and ControlM. Please let me know what is/isn't possible to do with these applications to create such a dashboard?

## ASSISTANT
Both SolarWinds and ControlM are powerful monitoring and automation tools that can help you create a dashboard to monitor the Document Archiver's performance. Here's a brief overview of what each tool can do, and how they can be utilized to create the dashboard:

**SolarWinds:**

SolarWinds is a comprehensive IT monitoring and management software that offers various modules to help monitor and manage different aspects of your IT infrastructure. For creating the Document Archiver dashboard, you can utilize the following SolarWinds modules:

1. *Server & Application Monitor (SAM):* SAM can help monitor the performance and status of your applications and servers, including the Document Archiver tool. You can create custom monitors and alerts for the Document Archiver, and even monitor specific metrics such as processing times, file transfers, and more.

2. *Network Performance Monitor (NPM):* NPM can help monitor the health and performance of your network infrastructure, which can be helpful in tracking file transfers between systems.

3. *Log Analyzer (LA):* LA can help collect, analyze, and alert on log data from various sources, including the Document Archiver. This can help you track specific events, such as the start and end times of the Contract Note process or other critical events.

**ControlM:**

ControlM is a powerful workload automation solution that can help orchestrate and monitor complex workflows across different platforms and applications. For creating the Document Archiver dashboard, you can utilize ControlM to:

1. *Automate checks and processes:* ControlM can help automate various checks and processes related to the Document Archiver, such as running the archiver hourly, polling for new files, or even starting the SFTP jobs.

2. *Monitor and alert on job statuses:* ControlM can help monitor the status of various jobs related to the Document Archiver, such as the Contract Note process or file transfers. You can create custom alerts based on job statuses, SLAs, or other metrics, and even send notifications to relevant stakeholders.

To create the dashboard with SolarWinds and ControlM, you will need to:

1. Set up appropriate monitors, alerts, and jobs in SolarWinds and ControlM to track the various metrics and processes related to the Document Archiver.

2. Use SolarWinds Orion Platform to create a custom dashboard that consolidates data from different SolarWinds modules and ControlM.

3. Add the necessary widgets, charts, and visualizations to the dashboard to display the data collected by SolarWinds and ControlM.

4. Configure the dashboard to automatically update and refresh based on the latest data from SolarWinds and ControlM.

By combining the capabilities of SolarWinds and ControlM, you should be able to create a comprehensive dashboard to monitor the Document Archiver's performance, as described in the previous response.

## USER
Can we go through setting this up in solarwinds please so that I can create a proof of concept dashboard please? 

## ASSISTANT
To set up a proof of concept dashboard in SolarWinds to monitor the Document Archiver, you'll need to follow these steps. Please note that the exact steps may vary depending on the SolarWinds version and modules you have installed.

1. **Set up Server & Application Monitor (SAM) component monitors:**
   First, you'll need to create custom component monitors in SAM to monitor the Document Archiver application. This may include monitoring services, processes, log files, and custom scripts to gather data about the Document Archiver's performance.

   a. Go to the "All Applications" page in the SAM module.
   
   b. Click on "Create New Template" and provide a name and description for your custom template, such as "Document Archiver Monitoring."

   c. Add component monitors to the template. You might use pre-built monitors like "Windows Service Monitor" to check the status of the Document Archiver service, or "Process Monitor" to monitor resource utilization. For more specific monitoring requirements, you may need to create custom script monitors to collect data from the Document Archiver directly.

   d. Assign the template to the appropriate server(s) where the Document Archiver is installed.

2. **Configure alerts and notifications:**
   Next, you'll want to set up custom alerts and notifications based on the data collected from the component monitors. This will help you stay informed about any issues or performance degradation in the Document Archiver.

   a. Navigate to the "Alerts & Activity" section in the SolarWinds Orion web console.

   b. Click on "Manage Alerts" and then "Add New Alert."

   c. Define the alert properties, such as name, description, severity, and trigger conditions based on the component monitors you've set up for the Document Archiver.

   d. Configure the alert actions, such as sending an email to the Application Support team or updating the status in the dashboard.

3. **Create a custom dashboard:**
   Now that you've set up the component monitors and alerts, it's time to create a custom dashboard to display the data.

   a. Go to the "Home" section in the SolarWinds Orion web console.

   b. Click on "Customize Page" and then "Add New Tab." Provide a name for the new tab, such as "Document Archiver Dashboard."

   c. Click on "Add Widgets" and search for the appropriate widgets to display the data from your component monitors and alerts. Some widgets you may want to consider include "Custom Chart," "Custom Table," "Alerts," and "AppStack Environment."

   d. Configure each widget to display the data from your component monitors and alerts related to the Document Archiver. You can customize the appearance, data sources, and time frames for each widget.

4. **Configure dashboard refresh settings:**
   Finally, you'll want to set the dashboard to automatically refresh and update based on the latest data.

   a. Click on "Settings" in the top right corner of the SolarWinds Orion web console.

   b. Go to "All Settings" and then "Web Console Settings."

   c. Set the "Auto-Refresh Interval" to your desired refresh rate, such as every 5 or 10 minutes.

With these steps, you should have a proof of concept dashboard in SolarWinds that monitors the Document Archiver's performance. You can further customize and refine the dashboard based on your requirements and the data you collect from the component monitors and alerts.