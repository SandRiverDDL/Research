# 发送给fresh reviewer的事实补充（send_message）

补充C03查新事实（无排序）：原证据中被阻的ICLR26 OPGD已通过官方 proceedings 取到原文：https://proceedings.iclr.cc/paper_files/paper/2026/file/1f8638a87bddd34e090698f0bfaa9c02-Paper-Conference.pdf 。§4/Algorithm1 PDF p8：先GAM梯度范数惩罚，再OGD+投影；任务结束释放旧梯度，用当前task model在全部历史样本上重算方向。未见保存J_old v→求J_new u匹配的步骤。官方摘要：https://proceedings.iclr.cc/paper_files/paper/2026/hash/1f8638a87bddd34e090698f0bfaa9c02-Abstract-Conference.html 。这补掉OPGD访问缺口，不等于整个functional transport邻域穷尽。会记录到证据文件。

附：实际补搜`"OPGD" "ICLR 2026" continual learning`、`"OGD+" "continual learning" "Jacobian" 2026`、`"Jacobian matching" "functional" "continual learning"`。PDF §4方法段、Alg1已读；非全文复读。
