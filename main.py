from Terminal import terminal_info, runner

while True:
    com = input(terminal_info.cur_dir + '> ')
    runner.run_com(com)
