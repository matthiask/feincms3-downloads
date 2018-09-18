import io
import subprocess
import tempfile


def preview_as_jpeg(path, *, geometry="300x300>"):
    with tempfile.TemporaryDirectory() as directory:
        cmd = ["convert", "-geometry", geometry, "-quality", "90"]

        if path.lower().endswith(".pdf"):
            cmd.extend(["-background", "white", "-alpha", "remove"])

        cmd.extend(["%s[0]" % path, "%s/pre.jpg" % directory])

        # print(cmd)
        ret = subprocess.call(cmd, env={"PATH": "/usr/local/bin:/usr/bin:/bin"})

        if ret == 0:
            with io.open("%s/pre.jpg" % directory, "rb") as f:
                return f.read()