import cmd2
import pytube
import os


class YouTubecmd(cmd2.Cmd):
    def __init__(self):
        pass



    def do_downLoad(self, args):
        """:arg
        tthis comnmand allows you downalod the video by id
        """
        myvideo = pytube.YouTube(args).streams.first().download()

    def do_setfolder(self, args):
        os.chdir(args)
        curfile = os.getcwd()
        print(f"the file path is currently {curfile}")

    def do_Info(self, args):
        myvideo = pytube.YouTube(args)
        info = f"""
        {myvideo.streams.fmt_streams}
        {myvideo.views}
        {myvideo.check_availability()}
        """
        print(info)


ytcli = YouTubecmd()
ytcli.cmdloop()
