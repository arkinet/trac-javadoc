import re
from trac.wiki.macros import WikiMacroBase
from trac.versioncontrol.api import RepositoryManager

class JavaDocMacro(WikiMacroBase):
	revision = "$Rev$"
	url = "$URL$"

	def expand_macro(self, formatter, name, args):
        	path = unicode(args)
	
		rm = RepositoryManager(self.env)

		for repo_name in rm.get_all_repositories():
			repo = rm.get_repository(repo_name)

			if repo.has_node(path):
				return self.get_javadoc(repo, repo_name, path)
		return "No file found for %s" % (path)

	def get_javadoc(self, repo, repo_name, path):
		src = repo.get_node(path).get_content()
		content = src.read()
		javadoc = ""
		class_found = False
		is_javadoc = False
		for line in content.split("\n"):
			line = line.strip()

			#check if end of comment
			if re.match("\\*\\/.*", line):
				is_javadoc = False

			#check if class declaration
			if re.match("(^|public |private |protected )(class|interface).*", line):
				class_found = True 

			#add line of javadoc, but remove the prepending *
			if is_javadoc:
				javadoc += re.search(".*?\\*+(.*)",line).group(1) + "\n"

			#check if start of comment
			if re.match("\\/\\*.*", line) and not class_found:
				is_javadoc = True

		#get filename without .java and full path
                filename = re.search(".*/(.*).java", path).group(1)
		
		return "<h3><a href='/browser/%s/%s'>%s</a></h3><pre class='wiki'>%s</pre>" % (repo_name, path, filename, javadoc)
