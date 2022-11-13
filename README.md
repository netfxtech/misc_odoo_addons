# netfx_odoo_addons
If using access_res_partner_contract and have the employees modules installed. It's very important you archive the rule: 
res.partner.rule.private.employee

It is required to make the module work if your record rules contain that rule by default.
Below is how your contact rules should appear in record rules.
![image](https://user-images.githubusercontent.com/62037189/201501727-7237c73a-30ac-4754-bf2f-b5faa4984976.png)
