## USER
In relation to the following, need to explain how the code produces the data in the table and what we would need to change in the code so that assets of excluded plans are not included in the asset class breakdown section of the valuation

Ticket:
292337 

From <http://camitsupportal/MRcgi/MRTicketPage.pl?USER=charper&MRP=1d9c4f8070573a4683fef0a215bfc221f&MAJOR_MODE=DETAILS&MAXMININC=&MRNUMBERLIST=295162%2C294641%2C292337%2C274661%2C273060%2C260497&LASTID=67398&ABN=&GRPDETAIL=&HISTORYKEY=&MR=292337&PROJECTID=10&RUNNING_IN_POPUP=1> 

I’ve had a couple of cases recently where the assets of excluded plans have been included in the asset class breakdown section of the valuation.
I’ve attached a report which shows the total current plan value as £659296.22 but the total in the asset class breakdown is £983139.61.
This was because the assets from a matured plan were included in the total – easy enough to remedy manually but I understand that this shouldn’t happen.

From <http://camitsupportal/tmp/charper_alldesc_61192.html> 



Needed info from user:
PAGE 6
Asset Class Breakdown 
YOUR FINANCIAL REVIEW
-
17 MARCH 2023
6
 
Asset class breakdown 
Asset Class
Weight (%) 
Value (GBP)
 
Equity
84.17%
£827,513.89
 
Fixed Interest
11.02%
£108,324.97
 
Cash
3.97%
£38,993.33
 
Other
0.35%
£3,430.34
 
Property
0.22%
£2,199.13
 
Alternative
0.16%
£1,537.79
 
Commodity
0.12%
£1,140.15
 
TOTALS
100.00% 
£983,139.61
 
Region
Weight (%)
Value (GBP)
 
UK
45.67%
£448,984.72
 
North America
25.59%
£251,551.76
 
Europe
12.27%
£120,601.64
 
Other
5.73%
£56,326.35
 
Emerging Markets
4.97%
£48,891.75
 
Asia Pacific
3.52%
£34,636.16
 
Japan
2.25%
£22,147.23
 
TOTALS
100.00% 
£983,139.61
 
-------------------------------------------------------

PAGE 5
YOUR FINANCIAL REVIEW
-
17 MARCH 2023
5
 
Policies - summary 
John Allenby
 
Total contributions
Total withdrawals
Current value
 
Stocks & Shares ISA
£228,011.29
£50,000.00
£335,544.11
 
OEIC
£341,694.71
£335,275.92
£323,752.11
 
Total
£569,706.00
£385,275.92
£659,296.22

-------------------------------------------------------

Code:
Login to XPLAN Live
Go to Settings, Site, Templates
Expand the 'Periodic Review' section and select the following
	Periodic Review
Click on the name of the template (this is currently 'CBAM Review Report v1.7.doc as of 2nd May 2023 for example)
Download the template in Microsoft Office Format
Open the template

/*

Asset class breakdown
<:let templist=[]:><:let portfoliotxt=’’:><:if cs == 1 and ps == 1 and js == 1:>
<:let portfoliotxt=’CX,PX,JX’:>
<:end:>
<:if cs == 1 and ps == 1 and js == 0:>
<:let portfoliotxt=’CX,PX’:>
<:end:>
<:if cs == 1 and ps == 0 and js == 1:>
<:let portfoliotxt=’CX,JX’:>
<:end:>
<:if cs == 1 and ps == 0 and js == 0:>
<:let portfoliotxt=’CX’:>
<:end:>
<:if cs == 0 and ps == 1 and js == 1:>
<:let portfoliotxt=’PX,JX’:>
<:end:>
<:if cs == 0 and ps == 1 and js == 0:>
<:let portfoliotxt=’PX’:>
<:end:>
<:if cs == 0 and ps == 0 and js == 1:>
<:let portfoliotxt=’JX’:>
<:end:>
<:for item in [x for x in $client.asset if str(x.exclude_from_review.text) in ['No','None']]:>
<:for account in item.linked_portfolio_accounts:> 
<:=templist.append(str(account.description)):> <:if x==1:>
<:end:>
<:end:>
<:end:>
<:for item in [x for x in $client.fund_za if str(x.policy_status.value) in ['Active','Premium Holiday'] and str(x.exclude_from_review.text) in ['No','None']]:>
<:for account in item.linked_portfolio_accounts:>
<:=templist.append(str(account.description)):> <:if x==1:>
<:end:>
<:end:>
<:end:>
<:if $partner:>
<:for item in [x for x in $partner.fund_za if str(x.policy_status.value) in ['Active','Premium Holiday'] and str(x.exclude_from_review.text) in ['No','None']]:>
<:for account in item.linked_portfolio_accounts:>
<:=templist.append(str(account.description)):> <:if x==1:>
<:end:>
<:end:>
<:end:>
<:end:>
 
<:let restrictsub=[]:><:let portfolios =[{‘subfund’:x[‘subfund’],‘unformatted_subfund_raw’:x[‘unformatted_subfund_raw’],’unformatted_portfolioid_raw’:x[‘unformatted_portfolioid_raw’],’unformatted_subfund_desc‘:x[‘unformatted_subfund_desc’]} for x in $client.DoReport.ipsv.any_report('value', report_source='holdings', portfolios=portfoliotxt, date=’Today’, subreports=[‘portfolioid’, ‘subfund’,'exchange', 'code'], exclude_subfunds=’on’)]:> <:for portfolioid in dict([(sr[‘unformatted_portfolioid_raw’], None) for sr in portfolios]):>
<:if portfolioid.startswith(‘J’):>
<:for item in $entity(int(portfolioid[1:])).portfolio_accounts(True):>
<:if str(item.subfund_desc) in templist:>
<:=restrictsub.append((str(item.ips_portfolio_id),str(item.ips_subfund_id))):> <:if x==1:>
<:end:>
<:end:>
<:end:>
<:else:>
<:for item in $entity(int(portfolioid[1:])).portfolio_accounts():>
<:if str(item.subfund_desc) in templist:>
<:=restrictsub.append((str(item.ips_portfolio_id),str(item.ips_subfund_id))):> <:if x==1:>
<:end:>
<:end:>
<:end:>
<:end:>
<:end:>
<:if len(restrictsub):>
<:=$client.DoReport.ips.assetallocation(portfolios=portfoliotxt, date='Today', exclude_subfunds='off', group='AAValue', width='10cm',sort='-weight', height='6cm', table_format='AATable', restrict_subfunds=restrictsub, custom_legend=1, legend_options={'position':'right', 'fields':'className,weight,value', 'field_titles':'Asset Class,Weight (%),Value (GBP)', 'field_widths':'50px,30px,50px', 'field_alignments':'left,right,right', 'display_total':1, 'display_decimal':1, 'display_dollar':1, 'display_percent':1, 'total_font_weight':'bold'}):>
 
<:=$client.DoReport.ips.regionalassetalloc_actual(portfolios=portfoliotxt, date= 'Today', restrict_subfunds=restrictsub, exclude_subfunds='off', group='AAValue', sort='-weight', table_format='AATable', charts={'regional':{'width':'10cm', 'height':'6cm', 'custom_legend':1, 'legend_options':{'position':'right', 'field_titles':'Region,Weight (%),Value (GBP)','fields':'title,weight,value', 'field_widths': '50px,30px,50px', 'field_alignments':'left,right,right', 'display_total':1, 'display_decimal':1, 'display_dollar':1, 'display_percent':1,'total_font_weight':'bold'}}}):>
<:else:>
You have not selected any accounts.
<:end:>
<:end #asset_class_breakdown in 1:>
<:if str($client.plan_and_fund_valuation) in [‘1’]:>
<:if len(c_assets1) or len(ppension1) or tempins==1:>
*/

-------------------------------------------------------

Based on the above information, I would like to create a troubleshooting guide on how to investigate such issues (an 'idiot-proof' guide, so to speak) and how to amend the code so that it fixes the reported problem (This was because the assets from a matured plan were included in the total) - how do you identify what bit of code this is related to and what needs to change so that assets from a matured plan are not included in the total. The code is XMERGE (similar to Python I believe).

## ASSISTANT
Based on the provided information and code, it seems that the issue is related to the asset class breakdown not properly excluding assets from matured plans. To create a troubleshooting guide, follow these steps:

1. Identify the cause of the issue: 
In this case, the issue is that assets from matured plans are being included in the asset class breakdown.

2. Locate the relevant part of the code: 
Look for the code section responsible for generating the asset class breakdown. In the provided code, it's the section starting with "Asset class breakdown" and ending with the comment "<:end #asset_class_breakdown in 1:>".

3. Investigate the issue: 
In the code, the assets are being filtered based on the "exclude_from_review" field and the "policy_status" field. The current filtering conditions are ['No', 'None'] for "exclude_from_review" and ['Active', 'Premium Holiday'] for "policy_status". It seems that the code is not considering the matured plans while filtering the assets.

4. Modify the code to fix the issue: 
To exclude assets from matured plans, you should update the filtering conditions for the "policy_status" field. Add a condition to exclude assets with a "Matured" status.

Here's how you can modify the relevant parts of the code:

Replace this line:

```python
<:for item in [x for x in $client.fund_za if str(x.policy_status.value) in ['Active','Premium Holiday'] and str(x.exclude_from_review.text) in ['No','None']]:>
```

With this line:

```python
<:for item in [x for x in $client.fund_za if str(x.policy_status.value) in ['Active','Premium Holiday'] and str(x.policy_status.value) != 'Matured' and str(x.exclude_from_review.text) in ['No','None']]:>
```

And replace this line:

```python
<:for item in [x for x in $partner.fund_za if str(x.policy_status.value) in ['Active','Premium Holiday'] and str(x.exclude_from_review.text) in ['No','None']]:>
```

With this line:

```python
<:for item in [x for x in $partner.fund_za if str(x.policy_status.value) in ['Active','Premium Holiday'] and str(x.policy_status.value) != 'Matured' and str(x.exclude_from_review.text) in ['No','None']]:>
```

These changes will ensure that assets from matured plans are not included in the asset class breakdown.

5. Test the updated code: 
After making the changes, test the code by running the report and verifying that the assets from matured plans are no longer included in the asset class breakdown.