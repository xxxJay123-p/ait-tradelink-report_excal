from bs4 import BeautifulSoup
import csv
html_data = """
<table class="soadetail">
        <thead>
        <tr>
          <th colspan="7">Unbilled Item Details</th>
        </tr>
        </thead>
        <tbody>
          <tr>
            <td class="header" colspan="6">Items Up To Last Charge Calculation <sup>*1</sup></td>
          </tr>
          <tr>
            <td class="field" width="100%">Item Description</td>
            <td class="field" nowrap="">Date</td>
            <td class="field" nowrap="">Unit Price</td>
            <td class="field" nowrap="">Unit</td>
            <td class="field" nowrap="">Qty.</td>
            <td class="field" nowrap="">Net Amount</td>
          </tr>



          <tr>
            <td class="value" width="100%">CASH PAYMENT<div style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Payment Ref. - <font class="soadtlvaluefont">4907711</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 30,000.00</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">-1</td>
            <td class="value" nowrap="" style="text-align:right;">-$ 30,000.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U1F)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U1F)<div id="divInfo1" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U2E)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U2E)<div id="divInfo2" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 169.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 169.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U3D)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U3D)<div id="divInfo3" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U4C)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U4C)<div id="divInfo4" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U5B)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U5B)<div id="divInfo5" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U6A)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U6A)<div id="divInfo6" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U79)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U79)<div id="divInfo7" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 62.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 62.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U88)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U88)<div id="divInfo8" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009U97)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009U97)<div id="divInfo9" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 32.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 32.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UA6)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UA6)<div id="divInfo10" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UB5)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UB5)<div id="divInfo11" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 107.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 107.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UC4)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UC4)<div id="divInfo12" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UD3)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UD3)<div id="divInfo13" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 36.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 36.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UF1)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UF1)<div id="divInfo14" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UE2)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UE2)<div id="divInfo15" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 74.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 74.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UG0)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UG0)<div id="divInfo16" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UHZ)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UHZ)<div id="divInfo17" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 112.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 112.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UIY)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UIY)<div id="divInfo18" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 199.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 199.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UJX)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UJX)<div id="divInfo19" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 109.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 109.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UKW)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UKW)<div id="divInfo20" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 22.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 22.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ULV)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ULV)<div id="divInfo21" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 10.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 10.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UMU)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UMU)<div id="divInfo22" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 34.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 34.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UNT)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UNT)<div id="divInfo23" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UOS)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UOS)<div id="divInfo24" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 19.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 19.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UPR)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UPR)<div id="divInfo25" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 45.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 45.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UQQ)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UQQ)<div id="divInfo26" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 46.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 46.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009URP)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009URP)<div id="divInfo27" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009USO)</td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009USO)<div id="divInfo28" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Import Form 1</font><br>Ref. # 1 -  <font class="soadtlvaluefont">S02029320</font></font></div></td>
            <td class="value" nowrap="">2024/08/15</td>
            <td class="value" nowrap="" style="text-align:right;">$ 128.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 128.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UTN)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UTN)<div id="divInfo29" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UUM)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UUM)<div id="divInfo30" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 89.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 89.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UVL)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UVL)<div id="divInfo31" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 162.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 162.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UWK)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UWK)<div id="divInfo32" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 47.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 47.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UXJ)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UXJ)<div id="divInfo33" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 159.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 159.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UYI)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UYI)<div id="divInfo34" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 161.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 161.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009UZH)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009UZH)<div id="divInfo35" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 28.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 28.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V09)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V09)<div id="divInfo36" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 5.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 5.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V18)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V18)<div id="divInfo37" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V27)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V27)<div id="divInfo38" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Import Form 1</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V36)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V36)<div id="divInfo39" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 25.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 25.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V45)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V45)<div id="divInfo40" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 23.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 23.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V54)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V54)<div id="divInfo41" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 3.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 3.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V63)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V63)<div id="divInfo42" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 1.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 1.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V72)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V72)<div id="divInfo43" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V81)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V81)<div id="divInfo44" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009V90)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009V90)<div id="divInfo45" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 94.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 94.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VAZ)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VAZ)<div id="divInfo46" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VCX)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VCX)<div id="divInfo47" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VBY)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VBY)<div id="divInfo48" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 53.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 53.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VDW)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VDW)<div id="divInfo49" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 21.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 21.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VFU)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VFU)<div id="divInfo50" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Import Form 1</font><br>Ref. # 1 -  <font class="soadtlvaluefont">S02035060</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VEV)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VEV)<div id="divInfo51" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 27.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 27.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VGT)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VGT)<div id="divInfo52" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Import Form 1</font><br>Ref. # 1 -  <font class="soadtlvaluefont">S02035061</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VHS)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VHS)<div id="divInfo53" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Import Form 1</font><br>Ref. # 1 -  <font class="soadtlvaluefont">S02035075</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VIR)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VIR)<div id="divInfo54" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 37.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 37.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VJQ)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VJQ)<div id="divInfo55" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VKP)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VKP)<div id="divInfo56" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VLO)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VLO)<div id="divInfo57" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 113.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 113.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VMN)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VMN)<div id="divInfo58" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 93.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 93.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VNM)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VNM)<div id="divInfo59" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VOL)</td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VOL)<div id="divInfo60" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/16</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VPK)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VPK)<div id="divInfo61" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 20.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 20.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VQJ)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VQJ)<div id="divInfo62" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 24.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 24.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VRI)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VRI)<div id="divInfo63" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 59.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 59.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VSH)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VSH)<div id="divInfo64" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VTG)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VTG)<div id="divInfo65" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 76.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 76.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VUF)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VUF)<div id="divInfo66" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 18.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 18.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VVE)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VVE)<div id="divInfo67" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 21.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 21.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VWD)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VWD)<div id="divInfo68" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 63.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 63.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VXC)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VXC)<div id="divInfo69" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VYB)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VYB)<div id="divInfo70" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 18.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 18.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009VZA)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009VZA)<div id="divInfo71" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 23.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 23.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W02)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W02)<div id="divInfo72" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W11)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W11)<div id="divInfo73" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W20)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W20)<div id="divInfo74" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W3Z)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W3Z)<div id="divInfo75" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 31.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 31.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W4Y)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W4Y)<div id="divInfo76" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 39.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 39.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W5X)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W5X)<div id="divInfo77" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 35.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 35.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W6W)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W6W)<div id="divInfo78" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W7V)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W7V)<div id="divInfo79" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 20.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 20.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W8U)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W8U)<div id="divInfo80" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font><br>Ref. # 1 -  <font class="soadtlvaluefont">HKG02031263</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009W9T)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009W9T)<div id="divInfo81" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WAS)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WAS)<div id="divInfo82" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WBR)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WBR)<div id="divInfo83" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WCQ)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WCQ)<div id="divInfo84" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 50.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 50.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WDP)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WDP)<div id="divInfo85" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WEO)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WEO)<div id="divInfo86" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 13.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 13.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WFN)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WFN)<div id="divInfo87" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 42.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 42.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WGM)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WGM)<div id="divInfo88" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 20.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 20.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WHL)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WHL)<div id="divInfo89" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 196.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 196.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WIK)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WIK)<div id="divInfo90" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 90.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 90.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WJJ)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WJJ)<div id="divInfo91" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 33.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 33.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WKI)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WKI)<div id="divInfo92" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 12.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 12.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WLH)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WLH)<div id="divInfo93" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 65.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 65.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WMG)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WMG)<div id="divInfo94" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 38.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 38.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WOE)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WOE)<div id="divInfo95" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 12.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 12.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WNF)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WNF)<div id="divInfo96" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 58.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 58.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WPD)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WPD)<div id="divInfo97" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 56.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 56.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WQC)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WQC)<div id="divInfo98" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 159.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 159.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WRB)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WRB)<div id="divInfo99" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 25.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 25.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WSA)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WSA)<div id="divInfo100" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WT9)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WT9)<div id="divInfo101" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 106.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 106.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WU8)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WU8)<div id="divInfo102" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WV7)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WV7)<div id="divInfo103" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WW6)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WW6)<div id="divInfo104" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 47.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 47.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WX5)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WX5)<div id="divInfo105" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 22.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 22.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WY4)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WY4)<div id="divInfo106" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009WZ3)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009WZ3)<div id="divInfo107" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 67.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 67.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X0V)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X0V)<div id="divInfo108" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 95.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 95.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X1U)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X1U)<div id="divInfo109" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X2T)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X2T)<div id="divInfo110" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 25.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 25.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X3S)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X3S)<div id="divInfo111" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 175.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 175.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X4R)</td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X4R)<div id="divInfo112" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/19</td>
            <td class="value" nowrap="" style="text-align:right;">$ 4.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 4.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X5Q)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X5Q)<div id="divInfo113" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 4.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 4.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X6P)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X6P)<div id="divInfo114" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 68.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 68.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X7O)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X7O)<div id="divInfo115" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 3.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 3.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X8N)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X8N)<div id="divInfo116" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009X9M)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009X9M)<div id="divInfo117" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XAL)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XAL)<div id="divInfo118" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 15.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 15.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XBK)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XBK)<div id="divInfo119" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 48.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 48.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XCJ)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XCJ)<div id="divInfo120" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 9.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 9.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XDI)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XDI)<div id="divInfo121" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 1.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 1.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XEH)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XEH)<div id="divInfo122" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 123.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 123.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XFG)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XFG)<div id="divInfo123" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 2.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XGF)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XGF)<div id="divInfo124" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XHE)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XHE)<div id="divInfo125" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 13.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 13.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XID)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XID)<div id="divInfo126" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 52.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 52.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XJC)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XJC)<div id="divInfo127" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XKB)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XKB)<div id="divInfo128" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XLA)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XLA)<div id="divInfo129" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 69.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 69.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XM9)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XM9)<div id="divInfo130" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XN8)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XN8)<div id="divInfo131" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XO7)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XO7)<div id="divInfo132" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 6.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 6.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XP6)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XP6)<div id="divInfo133" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 128.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 128.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XQ5)</td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XQ5)<div id="divInfo134" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/20</td>
            <td class="value" nowrap="" style="text-align:right;">$ 96.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 96.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XR4)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XR4)<div id="divInfo135" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 37.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 37.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XS3)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XS3)<div id="divInfo136" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 44.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 44.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XT2)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XT2)<div id="divInfo137" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 60.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 60.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XU1)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XU1)<div id="divInfo138" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 38.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 38.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XV0)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XV0)<div id="divInfo139" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XWZ)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XWZ)<div id="divInfo140" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 60.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 60.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XXY)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XXY)<div id="divInfo141" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 189.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 189.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XYX)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XYX)<div id="divInfo142" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 78.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 78.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009XZW)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009XZW)<div id="divInfo143" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 116.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 116.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y0O)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y0O)<div id="divInfo144" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 85.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 85.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y1N)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y1N)<div id="divInfo145" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 122.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 122.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y2M)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y2M)<div id="divInfo146" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 31.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 31.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y3L)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y3L)<div id="divInfo147" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y4K)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y4K)<div id="divInfo148" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y5J)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y5J)<div id="divInfo149" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y6I)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y6I)<div id="divInfo150" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y7H)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y7H)<div id="divInfo151" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 174.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 174.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y8G)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y8G)<div id="divInfo152" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Y9F)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Y9F)<div id="divInfo153" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YAE)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YAE)<div id="divInfo154" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 10.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 10.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YBD)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YBD)<div id="divInfo155" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YCC)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YCC)<div id="divInfo156" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 101.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 101.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YDB)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YDB)<div id="divInfo157" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 81.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 81.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YEA)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YEA)<div id="divInfo158" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 29.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 29.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YF9)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YF9)<div id="divInfo159" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YG8)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YG8)<div id="divInfo160" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YH7)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YH7)<div id="divInfo161" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YI6)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YI6)<div id="divInfo162" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Import Form 1</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 106.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 106.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YJ5)</td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YJ5)<div id="divInfo163" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font><br>Ref. # 1 -  <font class="soadtlvaluefont">HKG02038137</font></font></div></td>
            <td class="value" nowrap="">2024/08/21</td>
            <td class="value" nowrap="" style="text-align:right;">$ 104.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 104.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YK4)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YK4)<div id="divInfo164" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YL3)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YL3)<div id="divInfo165" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YM2)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YM2)<div id="divInfo166" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 8.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 8.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YN1)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YN1)<div id="divInfo167" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 84.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 84.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YO0)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YO0)<div id="divInfo168" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 7.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 7.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YPZ)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YPZ)<div id="divInfo169" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 1.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 1.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YQY)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YQY)<div id="divInfo170" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 8.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 8.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YRX)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YRX)<div id="divInfo171" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YSW)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YSW)<div id="divInfo172" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 102.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 102.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YTV)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YTV)<div id="divInfo173" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YUU)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YUU)<div id="divInfo174" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 19.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 19.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YVT)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YVT)<div id="divInfo175" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 59.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 59.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YWS)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YWS)<div id="divInfo176" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 38.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 38.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YXR)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YXR)<div id="divInfo177" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 119.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 119.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YYQ)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YYQ)<div id="divInfo178" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 11.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 11.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009YZP)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009YZP)<div id="divInfo179" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z0H)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z0H)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC PENALTY CHARGE (4A39KJEA009Z0H)<div id="divInfo180" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font><br>Ref. # 1 -  <font class="soadtlvaluefont">S01905421</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 40.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z1G)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z1G)<div id="divInfo181" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 113.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 113.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z2F)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z2F)<div id="divInfo182" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z3E)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z3E)<div id="divInfo183" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 137.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 137.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z4D)</td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z4D)<div id="divInfo184" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/22</td>
            <td class="value" nowrap="" style="text-align:right;">$ 7.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 7.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z5C)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z5C)<div id="divInfo185" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 7.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 7.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z6B)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z6B)<div id="divInfo186" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 64.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 64.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z7A)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z7A)<div id="divInfo187" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z89)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z89)<div id="divInfo188" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009Z98)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009Z98)<div id="divInfo189" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 18.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 18.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZA7)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZA7)<div id="divInfo190" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZB6)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZB6)<div id="divInfo191" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZC5)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZC5)<div id="divInfo192" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZD4)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZD4)<div id="divInfo193" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 4.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 4.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZE3)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZE3)<div id="divInfo194" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZF2)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZF2)<div id="divInfo195" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 145.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 145.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZG1)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZG1)<div id="divInfo196" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 51.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZH0)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZH0)<div id="divInfo197" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 5.90</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 5.90</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZIZ)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZIZ)<div id="divInfo198" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 94.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 94.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZJY)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZJY)<div id="divInfo199" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 23.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 23.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZKX)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZKX)<div id="divInfo200" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 140.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 140.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZLW)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZLW)<div id="divInfo201" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZMV)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZMV)<div id="divInfo202" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZNU)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZNU)<div id="divInfo203" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 27.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 27.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZOT)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZOT)<div id="divInfo204" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 39.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 39.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZPS)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZPS)<div id="divInfo205" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZQR)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZQR)<div id="divInfo206" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 3.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 3.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZRQ)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZRQ)<div id="divInfo207" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 181.50</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 181.50</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZSP)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZSP)<div id="divInfo208" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 30.70</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 30.70</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZTO)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZTO)<div id="divInfo209" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 0.20</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZUN)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZUN)<div id="divInfo210" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 65.10</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 65.10</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZVM)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZVM)<div id="divInfo211" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 149.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 149.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZWL)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZWL)<div id="divInfo212" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 190.40</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 190.40</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZXK)</td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZXK)<div id="divInfo213" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/23</td>
            <td class="value" nowrap="" style="text-align:right;">$ 57.60</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 57.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">TDEC TRANSACTION (4A39KJEA009ZYJ)</td>
            <td class="value" nowrap="">2024/08/24</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 16.60</td>
          </tr>

          <tr>
            <td class="value" width="100%">IMPORT/EXPORT DECLARATION CHARGE (4A39KJEA009ZYJ)<div id="divInfo214" style="padding: 0 0 0 20px;"><font class="soadtlfieldfont">Form Type -  <font class="soadtlvaluefont">Export Form 2</font></font></div></td>
            <td class="value" nowrap="">2024/08/24</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
            <td class="value" nowrap="" style="text-align:center;">-</td>
            <td class="value" nowrap="" style="text-align:center;">1</td>
            <td class="value" nowrap="" style="text-align:right;">$ 200.00</td>
          </tr>

          <tr><td colspan="7">&nbsp;</td></tr>
        </tbody>
      </table>
"""

def parse_html_data(html_data):
    # Parse the HTML data using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find the table with the class "soadetail"
    table = soup.find('table', class_='soadetail')

    # Extract the data from the table
    rows = table.find_all('tr')
    structured_data = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 6:
            # Extract the data from the cells
            item_description = cells[0].text.strip()
            date = cells[1].text.strip()
            unit_price_text = cells[2].text.strip('$ ')
            unit = cells[3].text.strip()
            qty_text = cells[4].text.strip()
            net_amount_text = cells[5].text.strip('$ ')

            # Check if the unit price and quantity can be converted to float
            try:
                unit_price = float(unit_price_text)
                qty = float(qty_text)
            except ValueError:
                continue  # Skip this row if the data is not in the expected format

            # Extract the transaction ID and form type from the item description
            transaction_id = item_description.split(' (')[1].split(')')[0]
            item_description = item_description.split(')')[1].strip()
            form_type = ""
            if "Form Type" in item_description:
                try:
                    form_type = item_description.split("Form Type - ")[1]
                except IndexError:
                    pass  # Skip this row if the format is not as expected

            # Split the date into year, month, and day
            year, month, day = date.split('/')

            # Determine the transaction type
            if "TDEC TRANSACTION" not in item_description:
                transaction_type = "IMPORT/EXPORT DECLARATION CHARGE"
                tdec_transaction = "16.6"
                import_export_charge = str(unit_price)
                tdec_clothing_levy = "0.0"
                tdec_penalty = "0.0"
                total = str(float(net_amount_text))

                # Only add the row if the total is not 16.6
                if total != "16.6":
                    structured_data.append([
                        f"{year}/{month}/{day}",
                        date,
                        transaction_id,
                        item_description,
                        "39958258001.TL",
                        "39958258001.TL",
                        form_type,
                        "",
                        "",
                        "",
                        "",
                        "",
                        "tmka92634",
                        tdec_transaction,
                        import_export_charge,
                        tdec_clothing_levy,
                        tdec_penalty,
                        total
                    ])

    return structured_data

data = parse_html_data(html_data)

# Add the header row
header = ["Statement Date", "Transaction Date", "UXR", "Item Description", "EDI Address", "Party ID", "Form Type", "Internal Reference #1", "Internal Reference #2", "Internal Reference #3", "Internal Reference #4", "Internal Reference #5", "User", "TDEC Transaction", "Import/Export Declaration Charge", "TDEC Clothing Levy Charge", "TDEC Penalty Charge", "Total"]
data.insert(0, header)

# Iterate through the data rows
for row in data[1:]:
    transaction_date = row[1]
    uxr = row[2]
    item_description = row[3]
    tdec_transaction = float(row[13])
    form_type = row[6]
    import_export_declaration_charge = float(row[14])

    # Append the data to the list
    data.append({
        'Statement Date': row[0],
        'Transaction Date': transaction_date,
        'UXR': uxr,
        'Item Description': item_description,
        'EDI Address': row[4],
        'Party ID': row[5],
        'Form Type': form_type,
        'Internal Reference #1': row[7],
        'Internal Reference #2': row[8],
        'Internal Reference #3': row[9],
        'Internal Reference #4': row[10],
        'Internal Reference #5': row[11],
        'User': row[12],
        'TDEC Transaction': tdec_transaction,
        'Import/Export Declaration Charge': import_export_declaration_charge,
        'TDEC Clothing Levy Charge': 0.0,
        'TDEC Penalty Charge': 0.0,
        'Total': tdec_transaction + import_export_declaration_charge
    })

# Write the data to a CSV file
if len(data) > 1:
    with open('tradelink_statement.csv', 'w', newline='') as csvfile:
        fieldnames = data[0]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data[1:]:
            if isinstance(row, dict):
                writer.writerow(row)

    print("CSV file generated: tradelink_statement.csv")
else:
    print("No data to write to the CSV file.")





