# TRLinkHelper

## 概述

TRLinkHelper 是一款基於 Python 的圖形用戶界面應用程序，旨在自動化處理貿易通帳單 Excel 文件、Cargowise Excel/CSV 報表以及可選的 HTML 文件。它將貿易通與 Cargowise 的交易數據進行匹配，生成詳細報表，並支持雙語（英文/中文）界面。主要功能包括：

- **Excel/CSV 處理**：將貿易通帳單交易與 Cargowise 數據進行匹配。
- **HTML 解析**：從 HTML 文件中提取交易詳情並整合到 Excel 報表中。
- **進度追蹤**：在處理過程中顯示進度條和百分比更新。
- **雙語支持**：可在英文和中文界面之間切換。
- **錯誤日誌**：將處理詳情和錯誤記錄到 `trlink_helper.log`。

由 [xxxJay123](https://github.com/xxxJay123) 開發，此工具為物流和貿易專業人士簡化了帳單對帳流程。

## 安裝

### 前置條件
- Python 3.8 或更高版本
- 所需的 Python 庫：
  ```bash
  pip install ttkbootstrap pandas openpyxl beautifulsoup4 chardet
  ```

### 設置
1. 克隆或下載倉庫：
   ```bash
   git clone https://github.com/xxxJay123-p/ait-tradelink-report_excal.git
   cd ait-tradelink-report_excal
   ```
2. 安裝依賴項：
   ```bash
   pip install -r requirements.txt
   ```
   創建一個 `requirements.txt` 文件，內容如下：
   ```
   ttkbootstrap
   pandas
   openpyxl
   beautifulsoup4
   chardet
   ```
3. 確保 `trlinkhelper.ico` 文件位於項目目錄中（可選，用於 Windows 圖標顯示）。
4. 運行應用程序：
   ```bash
   python TRLinkHelper_v3.1.1.py
   ```

## 使用指南

### 啟動應用程序
1. 運行 `python trlink_helper.py` 打開圖形用戶界面。
2. 界面默認為中文，可通過右上角的「Switch to English」按鈕切換為英文。

### 步驟1：輸入文件
1. **貿易通帳單 (Excel)**：點擊「瀏覽」選擇貿易通帳單 Excel 文件（`.xlsx`）。此文件為必填。
2. **Cargowise 數據 (Excel/CSV)**：點擊「瀏覽」選擇 Cargowise 報表，格式為 Excel（`.xlsx`）或 CSV（`.csv`）。此文件為必填。
3. **HTML 文件 (可選)**：點擊「瀏覽」選擇包含交易詳情的 HTML 文件（如適用）。

### 步驟2：HTML 處理設定
1. **使用 "截止日期後" 算法**：勾選此框（默認：啟用）以使用「EDI Transactions Since Last Charge Calculation」表格處理 HTML 數據。取消勾選則使用 `soadetail` 表格解析方法。
2. **TDEC 交易金額**：輸入 TDEC 交易金額（默認：16.6）。此值用於 HTML 交易計算。

### 步驟3：輸出設定
1. **輸出文件**：默認輸出文件為 `Tradelink_Bill_Report_<當前月份>.xlsx`。點擊「另存為」選擇自定義文件名或位置。
2. 如果輸出文件已存在，系統會提示是否覆蓋。

### 處理
1. 點擊「開始處理」啟動處理。進度條和百分比標籤將顯示，從 0% 更新到 100%。
2. 底部日誌區域顯示處理狀態，如「正在處理HTML文件...」或「正在處理Excel匹配...」。
3. 處理完成後，成功消息將顯示輸出文件路徑；若處理失敗，則顯示錯誤消息。

### 附加功能
- **語言切換**：使用右上角按鈕在英文和中文界面之間切換。
- **使用教學**：點擊「使用教學」打開在線文檔
- **ESC 按鈕**：點擊「ESC」退出應用程序。
- **錯誤日誌**：查看 `trlink_helper.log` 获取詳細的處理日誌。

### 輸出
輸出 Excel 文件包含：
- **交易詳情**：若提供 HTML 文件，則更新相關數據。
- **Tradelink 匹配結果**：貿易通交易詳情及匹配狀態。
- **Cargowise 匹配結果**：Cargowise 交易詳情及匹配狀態。

## 故障排除

- **進度條未顯示**：確保已選擇有效的貿易通和 Cargowise 文件。檢查 `trlink_helper.log` 是否有錯誤。
- **文件編碼問題**：應用程序使用 `chardet` 檢測 CSV 編碼。若出現錯誤，請確認 Cargowise CSV 為 UTF-8 或其他支持的編碼。
- **缺少列**：確保 Cargowise 文件包含交易編號、未清金額和工作編號列（不區分大小寫）。
- **圖標錯誤 (Windows)**：若缺少 `trlinkhelper.ico`，請從代碼中移除 `self.root.iconbitmap('trlinkhelper.ico')`。
- **依賴項**：確認已安裝所有必需庫（`ttkbootstrap`、`pandas`、`openpyxl`、`beautifulsoup4`、`chardet`）。
- **聯繫**：如有問題，請檢查日誌文件並聯繫開發者：[jay6677884@gmail.com]/[jcheng@aitworldwide.com]。

## 許可證

本項目採用 MIT 許可證。詳情請見 [LICENSE](./LICENSE) 文件。
