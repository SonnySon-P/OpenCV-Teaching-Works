# 課程一

**教學主題：** 架設開發環境
	
**目的：** 學習掌握Anaconda的操作技巧，建立並管理虛擬環境，同時熟練運用套件管理系統。

**操作解說：** 以下是本次課程的操作指引，請依照以下步驟進行：
1. 安裝Anaconda：請前往[官方網站](https://www.anaconda.com/download)下載該軟體，並按照圖形介面的指示完成安裝。
2. 開啟CLI視窗，進行Anaconda操作。
3. 設定Anaconda虛擬環境時常用的指令如下：
   ```shell
   conda env list  # 查看已建立的虛擬環境
   conda create -n learningEnv python=3.12  # 建立虛擬環境，learningEnv是環境名稱
   conda activate learningEnv  # 啟動虛擬環境
   conda deactivate  # 離開虛擬環境
   conda env remove --name learningEnv --all  # 刪除虛擬環境
   ```
4. 啟動Visual Studio Code，作為程式編輯的開發環境，並在其中開啟終端機。
5. 設定課程所需套件時常用的指令如下：
   ```shell
   conda list  # 列出虛擬環境下已安裝的所有套件
   conda install numpy  # 安裝套件，numpy是套件名稱
   conda uninstall numpy  # 刪除套件
   ```
