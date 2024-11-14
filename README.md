# conllx_df
A suite of tools that manipulate CoNLL-X/U files, with a focus on Arabic script.

## Introduction
The core of the package is the CoNLL-X class from the paper <a href="http://aclanthology.org/W06-2920.pdf"><i>CoNLL-X shared task on Multilingual Dependency Parsing</i></a>.

Since CoNLL-U is a more generalized version of CoNLL-U, CoNLL-U files can be used.

## Data restrictions
<ul>
<li>Currently, cycles are flagged as incorrect</li>
<li>UTF-8 is the default encoding*</li>
<li>If a tokens parent is the root node, '---' will be placed in the DEPREL column** </li>

</ul>

<sub>* Some files may contain special characters (i.e. emoticons) that only work with latin-1 encoding. There may be a workaround using this enconding if UTF-8 does not work.</sub>
<sub>** CoNLL-X uses ROOT instead of ---. A setting to select this may be added later.</sub>