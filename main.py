from Terminal import terminal_info, runner

while True:
    com = terminal_info.get_str_terminal_input(terminal_info.cur_dir)
    runner.run_com(com)
