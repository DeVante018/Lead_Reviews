WERKZEUG REPORT
Werkzeug (LIBRARY)
What does this technology (library/framework/service) accomplish for you?
    We used its secure_filename function to make sure filenames of the files users can upload are not malicious.
How does this technology accomplish what it does?
    Explanation for secure_filename entailed below

What license(s) or terms of service apply to this technology?

Werkzeug is licensed under the BSD 3-Clause "New" or "Revised" License which allows redistribution and use of the source code as long as the conditions, as found on the repo, are met:
https://github.com/pallets/werkzeug/blob/master/LICENSE.rst 
Copyright 2007 Pallets
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
1.  Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
2.  Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
3.  Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

To summarize: it is basically saying that we can use the library/source code however we want as long as we mention the copyright, its list of conditions, and the copyright disclaimer somewhere in our project.





Functionality of Werkzeug
Secure_filename():
What does this technology (library/framework/service) accomplish for you?
    The secure_filename function helps us maintain security in filenames of uploaded files as it is a way for an uploaded file to have a “safe” name. What does “safe” mean in this context? This function makes sure  the file name that is being uploaded does not contain spaces or checks to make sure the name of the file itself isn't something malicious. For example  “../../../admin/passwords”. If it is deemed to be unsafe, a new name will be generated but it is up to us to verify that this new name is indeed unique. This function will also allow file names to mostly, if not completely maintain the original naming convention if deemed safe.

How does this technology accomplish what it does? 

Secure_filename source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/utils.py#L430

The secure_filename function is located in the utils.py file of the werkzeug library and by passing a filename string into it, it will normalize it using the unicodedata module that is predefined in the python standard library (documentation: https://docs.python.org/3/library/unicodedata.html#module-unicodedata ), then it will encode the filename into ascii while ignoring the errors that may pop up, and then decode it from ascii back into plain text. Then the secure_filename function will iterate through separation character, sep, that is in the os.path.sep and os.path.altsep and replace them with a empty string and then get then stringified compilation of the filename using the _compile function located in the re.py file of the python standard library (source code: https://github.com/python/cpython/blob/1326f51bfc276102b7d011bedc1b759712e62a4a/Lib/re.py#L289 ) after adding “_” between each character in the filename string, then it will strip all instances of “._” from the compiled and stringified filename and update the old filename variable with the new filename. After that, it will check if the os name is “nt” and if the filename and its capitalized equivalent exist within the _windows_device_files variable in the same util.py file which holds a list of tuples (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/utils.py#L34). If the conditions pass, then secure _filename will format the filename string. Then it will finally return the filename that is safe to be used.


