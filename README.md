#	PHP 7 文件包含

此环境为 php 7 利用 segmentfault bug 制造临时文件构成 LFI 漏洞的实验环境。

题目参考了某次比赛的代码。侵删。

tmp 目录为 /tmp

Hack4fun : )

##  Session LFI
需要开启 `session.upload_progress.enabled` ，反序列化 handler 需要为 php 或者 php_serialize
直接根据`PHPSESSID=a`包含
需要知道 session 临时文件目录：
*   /var/lib/php/sess_PHPSESSID
*   /var/lib/php/sessions/sess_PHPSESSID
*   /tmp/sess_PHPSESSID
*   /tmp/sessions/sess_PHPSESSID

session 临时文件内容根据 session.handler 设置进行存储

## TMP LFI
可以在 phpinfo 界面看到上传的临时文件名字，进行包含。临时文件内容与上传文件内容一致