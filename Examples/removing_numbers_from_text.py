def sanitize_file(source, output):
    import re
    with open(source, "r") as fh:
        v_readfile = fh.read()
        v_readfile = re.sub(r'\d', '', v_readfile)
    with open(output, "w") as fh:
        fh.write(v_readfile)
