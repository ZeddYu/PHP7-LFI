<?php
$a = @$_GET['file'];
if (!$a) {
    highlight_file(__FILE__);
    die();
}
if (strpos($a,'flag')!==false) {
	die('nonono');
}
include $a;
?>