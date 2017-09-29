#!/usrbin/env python3
# import dislines
import responseclass

def main(ENV):
    r = responseclass.httpresp()
    r.setHeader("MaxCache", "0")
    r.content = """<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<title>Ejemplo de documento...</title>
 <p>...con un <a href="http://www.w3c.org">grado de purismo</a>
 sencillamente <em>*impresionante*</em>
 </p>"""
    return r
