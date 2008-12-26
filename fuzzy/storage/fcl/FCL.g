/** 
    Grammar definition for FCL used fuzzy.fcl.Reader of pyfuzzy 
*/
grammar FCL;

options {
	language=Python;
}
@header {
import fuzzy.System
import fuzzy.InputVariable
import fuzzy.OutputVariable
import fuzzy.Adjective
import fuzzy.set.Polygon
import fuzzy.set.Singleton
import fuzzy.defuzzify.COG
import fuzzy.defuzzify.COGS
import fuzzy.defuzzify.MaxLeft
import fuzzy.defuzzify.MaxRight
import fuzzy.operator.Not
import fuzzy.operator.Input
import fuzzy.operator.Compound
import fuzzy.Rule
import fuzzy.norm.Min
import fuzzy.norm.Max

def getNorm(name,p=None):
	m=__import__("fuzzy.norm."+name,fromlist=[name])
	c=m.__dict__[name]
	if p is None:
		return c()
	else:
		return c(p)
}
@init {
self.System = None
}
@members {
# test
}

main returns [system]	:	{self.System = None;} function_block_declaration {$system = self.System;};

function_block_declaration 
	: 
		'FUNCTION_BLOCK' 
		function_block_name { self.System = fuzzy.System.System(description=$function_block_name.text); }
		fb_io_var_declarations*
		//other_var_declarations*
		function_block_body
		'END_FUNCTION_BLOCK' 
		EOF
	;

fb_io_var_declarations 
	: input_declarations 
	| output_declarations
	;

input_declarations : 'VAR_INPUT' var_decl[0]+ 'END_VAR'; //see IEC 1131-3 Annex B
output_declarations : 'VAR_OUTPUT' var_decl[1]+ 'END_VAR';//see IEC 1131-3 Annex B

var_decl[output_var]
	:	 
		Identifier 
		':' 
		type 
		';' 
{
if $output_var == 0:
	self.System.variables[$Identifier.text]=fuzzy.InputVariable.InputVariable()
else:
	self.System.variables[$Identifier.text]=fuzzy.OutputVariable.OutputVariable()
}; // Rene

type 	:	 'REAL'; // Rene

	
other_var_declarations : var_declarations;

var_declarations : ;//see IEC 1131-3 Annex B


function_block_body 
	: 
	  fuzzify_block*
	  defuzzify_block*
   	  rule_block*
	  option_block*
	;

fuzzify_block 
	: 
	  'FUZZIFY' 
	  variable_name
	  linguistic_term[$variable_name.text]*
	  'END_FUZZIFY'
	;

defuzzify_block 
	: 
	  'DEFUZZIFY' 
	  f_variable_name
	  linguistic_term[$f_variable_name.text]*
	  accumulation_method
	  defuzzification_method[$f_variable_name.text]
	  default_value[$f_variable_name.text]?
	  range?
	  'END_DEFUZZIFY'
	;
	
rule_block 
	: 
	  'RULEBLOCK' 
	  	rule_block_name
	  	operator_definition*
	  	activation_method?
	  	rule[$rule_block_name.text]*
	  'END_RULEBLOCK';

option_block : 'OPTION'
 //any manufacturere specific parameter
'END_OPTION';

linguistic_term [var_name]
	: 
	'TERM' term_name ':=' membership_function ';' 
{
self.System.variables[$var_name].adjectives[$term_name.text]=fuzzy.Adjective.Adjective($membership_function.set);
}
;

membership_function returns [set]
	: 
		singleton {$set = $singleton.set;} 
	| 
		points {$set = $points.set;}
	;

singleton returns [set] 
	: 
		numeric_literal {$set = fuzzy.set.Singleton.Singleton(float($numeric_literal.text));} 
	| 
		variable_name
	;

points returns [set]
@init {
p=[]
}
	:
 	(
 		'(' 
 		(x=numeric_literal | variable_name) 
 		',' 
 		y=numeric_literal 
 		')' 
 		{p.append((float($x.text),float($y.text)));} 
 	)* 
 	{$set = fuzzy.set.Polygon.Polygon(p);} 
 	;

defuzzification_method [var_name] : 
	'METHOD' ':' 
	('COG' {self.System.variables[$var_name].defuzzy = fuzzy.defuzzify.COG.COG();}
	| 'COGS' {self.System.variables[$var_name].defuzzy = fuzzy.defuzzify.COGS.COGS();}
	| 'COA' 
	| 'LM' {self.System.variables[$var_name].defuzzy = fuzzy.defuzzify.MaxLeft.MaxLeft();}
	| 'RM' {self.System.variables[$var_name].defuzzy = fuzzy.defuzzify.MaxRight.MaxRight();}
	)
	';'
	;

default_value [var_name] : 
	'DEFAULT' ':=' 
	(
		numeric_literal {self.System.variables[$var_name].defuzzy.failsafe = float($numeric_literal.text);}
	| 
		'NC' {self.System.variables[$var_name].defuzzy.failsafe = None;}
	) 
	';'
	;

range : 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';';

operator_definition : (('OR' ':' ('MAX' | 'ASUM' | 'BSUM')) |
('AND' ':' ('MIN' | 'PROD' | 'BDIF'))) ';';

activation_method : 'ACT' ':' ('PROD' | 'MIN') ';';

accumulation_method : 'ACCU' ':' ('MAX' | 'BSUM' | 'NSUM') ';';

condition returns [input]
	: (s1=subcondition {$input = $s1.input}| variable_name) 
		(
			('AND' (s2=subcondition {$input = fuzzy.operator.Compound.Compound(fuzzy.norm.Min.Min(),$input,$s2.input);} | variable_name))+
		|
			('OR' (s3=subcondition {$input = fuzzy.operator.Compound.Compound(fuzzy.norm.Min.Min(),$input,$s3.input);} | variable_name))+
		)?
	;

subcondition returns [input]
	: ('NOT' '(' subcondition2 ')' {$input = fuzzy.operator.Not.Not($subcondition2.input);}) 
	| ( subcondition2 {$input = $subcondition2.input;})
	;

subcondition2 returns [input]
	: ('(' c1=condition ')' {$input = $c1.input;}) 
	| ( variable_name 'IS' x='NOT'? term_name {
$input = fuzzy.operator.Input.Input(self.System.variables[$variable_name.text].adjectives[$term_name.text])
if x is not None:
	$input = fuzzy.operator.Not.Not($input)
})
	| i1=Identifier ('[' param=numeric_literal ']')? '(' c4=condition ',' c5=condition ')' {
if $param.text is not None:
	p = float($param.text)
else:
	p = None
$input = fuzzy.operator.Compound.Compound(getNorm($i1.text,p),$c4.input,$c5.input);
	}// funktionsaufruf
	;

conclusion returns  [adj]
	: ( conclusion2 ',')*
		c2=conclusion2 {$adj=$c2.adj;}
	;

conclusion2 returns  [adj]
	: (
	 '(' c2=conclusion3  ')' {$adj=$c2.adj;} )
	| (     c1=conclusion3     {$adj=$c1.adj;} )
	;

conclusion3 returns  [adj]
	: (variable_name | (v2=variable_name 'IS' t2=term_name {$adj=self.System.variables[$v2.text].adjectives[$t2.text];}))
	;


rule [block_name]
@init{
certainty = 1.0
} : 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ('WITH' weighting_factor {certainty = float($weighting_factor.text);})? ';'
{
input = $condition.input
adjective = $conclusion.adj
self.System.rules[$block_name+'.'+$Integer_literal.text] = fuzzy.Rule.Rule(adjective,input,certainty=certainty)
}
;

weighting_factor : variable | numeric_literal;

function_block_name : Identifier;

rule_block_name : Identifier ;
term_name : Identifier ;
f_variable_name : Identifier ;
variable_name : Identifier;
numeric_literal : Integer_literal | Real_literal ;

variable 
	:	 variable_name; //????


Identifier : LETTER (LETTER|DIGIT)*;//see IEC 1131-3 Annex B

fragment Integer_literal_wo_sign
	: DIGIT+;
Integer_literal
	:	
		('+'|'-')? Integer_literal_wo_sign ;// ???? see IEC 1131-3 Annex B
		
fragment LETTER	: 'A'..'Z'|'a'..'z'|'_';	
fragment DIGIT	: '0'..'9';	

Real_literal
	:	Integer_literal '.' Integer_literal_wo_sign (('e'|'E') Integer_literal)?;//see IEC 1131-3 Annex B

WS  :  (' '|'\r'|'\t'|'\u000C'|'\n') {$channel=HIDDEN;}
    ;

COMMENT
    :   '(*' ( options {greedy=false;} : . )* '*)' {$channel=HIDDEN;}
    ;
