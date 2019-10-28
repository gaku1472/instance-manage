# Cloud FunctionでGCEインスタンス操作
GCEインスタンスの自動起動・停止を以下を用いて実現しました。  
・Cloud Function  
・Cloud Pub/Sub  
・Cloud Scheduler  

## Cloud Functionの設定
souce/start-instance.pyとstop-instance.pyで  
それぞれの関数を作成してください。

スクリプト内のprojectは適宜、書き換えをお願いします。  
トリガーはPub/Subを使用して、任意のトピックを作成してください。  

## Cloud Schedulerの設定
Cloud Schedulerを選択し、ジョブを作成します。
以下のように作成してください。

起動ジョブ：
　頻度：任意の時間帯
　ターゲット：Pub/Sub
　トピック：start-instance.pyを起動させるトピック
　ペイロード：{"instance_name":"gce instance name", "zone":"gce instance zone"}
