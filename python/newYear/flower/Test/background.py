def bgpic(self, picname=None):
    """Set background image or return name of current backgroundimage.

    Optional argument:
    picname -- a string, name of a gif-file or "nopic".

    If picname is a filename, set the corresponding image as background.
    If picname is "nopic", delete backgroundimage, if present.
    If picname is None, return the filename of the current backgroundimage.

    Example (for a TurtleScreen instance named screen):
    >>> screen.bgpic()
    'nopic'
    >>> screen.bgpic("landscape.gif")
    >>> screen.bgpic()
    'landscape.gif'
    """
    if picname is None:
        return self._bgpicname
    if picname not in self._bgpics:
        self._bgpics[picname] = self._image(picname)
    self._setbgpic(self._bgpic, self._bgpics[picname])
    self._bgpicname = picname