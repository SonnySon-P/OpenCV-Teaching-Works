# 課程一

**教學主題：** 架設開發環境
	
**目的：** 學習掌握Anaconda的操作技巧，建立並管理虛擬環境，同時熟練運用套件管理系統。

**操作解說：** 以下是本次課程的操作指引，請依照以下步驟進行：
1. 安裝Anaconda：請前往官方網站下載該軟體，並按照安裝精靈的指示完成安裝。
2. 開啟CLI(終端機)視窗，進行Anaconda操作。
3. 建立Anaconda虛擬環境，以下為操作時常用的指令：
   '''shell
   conda env list  # 查看已建立的虛擬環境
   conda create -n learningEnv python=3.12  # 建立虛擬環境，learningEnv是環境名稱，3.12是python的發行版本
   conda activate learningEnv  # 啟動虛擬環境
   conda deactivate  # 離開虛擬環境
   conda env remove --name learningEnv --all  # 刪除虛擬環境
   '''
4. 開啟Visual Studio Code作為程式編輯器，並在其中開啟終端機。
5. 安裝課程所需套件，以下為操作時常用的指令：
   '''shell
   conda list  # 列出虛擬環境下已安裝的所有套件
   conda install numpy  # 安裝套件，numpy是套件名稱
   conda uninstall numpy  # 刪除套件  
   '''
