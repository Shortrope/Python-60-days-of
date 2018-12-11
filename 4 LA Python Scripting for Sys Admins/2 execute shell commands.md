# subprocess

## subprocess.run()
invoke cmd and wait

    import subprocess
    proc = subprocess.run(["ls", "-l"])
    >>> proc
    CompletedProcess(args... , returncode=0)
    >>>

    proc = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    >>> proc
    >>> print(proc.stdout)
    >>> print(proc.stdout.decode())


    bytes.decode()

## Subprocess raise errer
raise an error if not successeful - check = True

    proc = subprocess.run(["ls", "-l"], check=True)

## subprocess.Popen()