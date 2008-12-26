# $ANTLR 3.1.1 FCL.g 2008-12-16 21:23:47

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
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



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
Real_literal=6
T__27=27
T__26=26
T__25=25
T__24=24
LETTER=7
T__23=23
T__22=22
T__21=21
T__20=20
T__61=61
T__60=60
EOF=-1
Identifier=4
T__55=55
T__56=56
T__19=19
T__57=57
T__58=58
T__16=16
T__51=51
T__52=52
T__15=15
T__53=53
T__18=18
T__54=54
T__17=17
Integer_literal_wo_sign=9
T__12=12
T__14=14
T__13=13
T__59=59
DIGIT=8
COMMENT=11
T__50=50
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
T__48=48
T__49=49
T__30=30
T__31=31
T__32=32
WS=10
T__33=33
T__34=34
Integer_literal=5
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "Identifier", "Integer_literal", "Real_literal", "LETTER", "DIGIT", 
    "Integer_literal_wo_sign", "WS", "COMMENT", "'FUNCTION_BLOCK'", "'END_FUNCTION_BLOCK'", 
    "'VAR_INPUT'", "'END_VAR'", "'VAR_OUTPUT'", "':'", "';'", "'REAL'", 
    "'FUZZIFY'", "'END_FUZZIFY'", "'DEFUZZIFY'", "'END_DEFUZZIFY'", "'RULEBLOCK'", 
    "'END_RULEBLOCK'", "'OPTION'", "'END_OPTION'", "'TERM'", "':='", "'('", 
    "','", "')'", "'METHOD'", "'COG'", "'COGS'", "'COA'", "'LM'", "'RM'", 
    "'DEFAULT'", "'NC'", "'RANGE'", "'..'", "'OR'", "'MAX'", "'ASUM'", "'BSUM'", 
    "'AND'", "'MIN'", "'PROD'", "'BDIF'", "'ACT'", "'ACCU'", "'NSUM'", "'NOT'", 
    "'IS'", "'['", "']'", "'RULE'", "'IF'", "'THEN'", "'WITH'"
]




class FCLParser(Parser):
    grammarFileName = "FCL.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
            )



               
        self.System = None




                


        

              
    # test



    # $ANTLR start "main"
    # FCL.g:42:1: main returns [system] : function_block_declaration ;
    def main(self, ):

        system = None

        try:
            try:
                # FCL.g:42:23: ( function_block_declaration )
                # FCL.g:42:25: function_block_declaration
                pass 
                #action start
                self.System = None;
                #action end
                self._state.following.append(self.FOLLOW_function_block_declaration_in_main44)
                self.function_block_declaration()

                self._state.following.pop()
                #action start
                system =  self.System
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return system

    # $ANTLR end "main"


    # $ANTLR start "function_block_declaration"
    # FCL.g:44:1: function_block_declaration : 'FUNCTION_BLOCK' function_block_name ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF ;
    def function_block_declaration(self, ):

        function_block_name1 = None


        try:
            try:
                # FCL.g:45:2: ( 'FUNCTION_BLOCK' function_block_name ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF )
                # FCL.g:46:3: 'FUNCTION_BLOCK' function_block_name ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF
                pass 
                self.match(self.input, 12, self.FOLLOW_12_in_function_block_declaration59)
                self._state.following.append(self.FOLLOW_function_block_name_in_function_block_declaration64)
                function_block_name1 = self.function_block_name()

                self._state.following.pop()
                #action start
                self.System = fuzzy.System.System(description=((function_block_name1 is not None) and [self.input.toString(function_block_name1.start,function_block_name1.stop)] or [None])[0]); 
                #action end
                # FCL.g:48:3: ( fb_io_var_declarations )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 14 or LA1_0 == 16) :
                        alt1 = 1


                    if alt1 == 1:
                        # FCL.g:48:3: fb_io_var_declarations
                        pass 
                        self._state.following.append(self.FOLLOW_fb_io_var_declarations_in_function_block_declaration70)
                        self.fb_io_var_declarations()

                        self._state.following.pop()


                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_function_block_body_in_function_block_declaration78)
                self.function_block_body()

                self._state.following.pop()
                self.match(self.input, 13, self.FOLLOW_13_in_function_block_declaration82)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_function_block_declaration87)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "function_block_declaration"


    # $ANTLR start "fb_io_var_declarations"
    # FCL.g:55:1: fb_io_var_declarations : ( input_declarations | output_declarations );
    def fb_io_var_declarations(self, ):

        try:
            try:
                # FCL.g:56:2: ( input_declarations | output_declarations )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 14) :
                    alt2 = 1
                elif (LA2_0 == 16) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # FCL.g:56:4: input_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_input_declarations_in_fb_io_var_declarations99)
                    self.input_declarations()

                    self._state.following.pop()


                elif alt2 == 2:
                    # FCL.g:57:4: output_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_output_declarations_in_fb_io_var_declarations105)
                    self.output_declarations()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "fb_io_var_declarations"


    # $ANTLR start "input_declarations"
    # FCL.g:60:1: input_declarations : 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR' ;
    def input_declarations(self, ):

        try:
            try:
                # FCL.g:60:20: ( 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR' )
                # FCL.g:60:22: 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR'
                pass 
                self.match(self.input, 14, self.FOLLOW_14_in_input_declarations115)
                # FCL.g:60:34: ( var_decl[0] )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == Identifier) :
                        alt3 = 1


                    if alt3 == 1:
                        # FCL.g:60:34: var_decl[0]
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_input_declarations117)
                        self.var_decl(0)

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(self.input, 15, self.FOLLOW_15_in_input_declarations121)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "input_declarations"


    # $ANTLR start "output_declarations"
    # FCL.g:61:1: output_declarations : 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR' ;
    def output_declarations(self, ):

        try:
            try:
                # FCL.g:61:21: ( 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR' )
                # FCL.g:61:23: 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR'
                pass 
                self.match(self.input, 16, self.FOLLOW_16_in_output_declarations129)
                # FCL.g:61:36: ( var_decl[1] )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == Identifier) :
                        alt4 = 1


                    if alt4 == 1:
                        # FCL.g:61:36: var_decl[1]
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_output_declarations131)
                        self.var_decl(1)

                        self._state.following.pop()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                self.match(self.input, 15, self.FOLLOW_15_in_output_declarations135)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "output_declarations"


    # $ANTLR start "var_decl"
    # FCL.g:63:1: var_decl[output_var] : Identifier ':' type ';' ;
    def var_decl(self, output_var):

        Identifier2 = None

        try:
            try:
                # FCL.g:64:2: ( Identifier ':' type ';' )
                # FCL.g:65:3: Identifier ':' type ';'
                pass 
                Identifier2=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_var_decl149)
                self.match(self.input, 17, self.FOLLOW_17_in_var_decl154)
                self._state.following.append(self.FOLLOW_type_in_var_decl159)
                self.type()

                self._state.following.pop()
                self.match(self.input, 18, self.FOLLOW_18_in_var_decl164)
                #action start
                 
                if output_var == 0:
                	self.System.variables[Identifier2.text]=fuzzy.InputVariable.InputVariable()
                else:
                	self.System.variables[Identifier2.text]=fuzzy.OutputVariable.OutputVariable()

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "var_decl"


    # $ANTLR start "type"
    # FCL.g:76:1: type : 'REAL' ;
    def type(self, ):

        try:
            try:
                # FCL.g:76:7: ( 'REAL' )
                # FCL.g:76:10: 'REAL'
                pass 
                self.match(self.input, 19, self.FOLLOW_19_in_type178)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "type"


    # $ANTLR start "other_var_declarations"
    # FCL.g:79:1: other_var_declarations : var_declarations ;
    def other_var_declarations(self, ):

        try:
            try:
                # FCL.g:79:24: ( var_declarations )
                # FCL.g:79:26: var_declarations
                pass 
                self._state.following.append(self.FOLLOW_var_declarations_in_other_var_declarations189)
                self.var_declarations()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "other_var_declarations"


    # $ANTLR start "var_declarations"
    # FCL.g:81:1: var_declarations : ;
    def var_declarations(self, ):

        try:
            try:
                # FCL.g:81:18: ()
                # FCL.g:81:20: 
                pass 



            finally:
                pass
        finally:

            pass

        return 

    # $ANTLR end "var_declarations"


    # $ANTLR start "function_block_body"
    # FCL.g:84:1: function_block_body : ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )* ;
    def function_block_body(self, ):

        try:
            try:
                # FCL.g:85:2: ( ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )* )
                # FCL.g:86:4: ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )*
                pass 
                # FCL.g:86:4: ( fuzzify_block )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 20) :
                        alt5 = 1


                    if alt5 == 1:
                        # FCL.g:86:4: fuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_fuzzify_block_in_function_block_body211)
                        self.fuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop5


                # FCL.g:87:4: ( defuzzify_block )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 22) :
                        alt6 = 1


                    if alt6 == 1:
                        # FCL.g:87:4: defuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_defuzzify_block_in_function_block_body217)
                        self.defuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop6


                # FCL.g:88:7: ( rule_block )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 24) :
                        alt7 = 1


                    if alt7 == 1:
                        # FCL.g:88:7: rule_block
                        pass 
                        self._state.following.append(self.FOLLOW_rule_block_in_function_block_body226)
                        self.rule_block()

                        self._state.following.pop()


                    else:
                        break #loop7


                # FCL.g:89:4: ( option_block )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 26) :
                        alt8 = 1


                    if alt8 == 1:
                        # FCL.g:89:4: option_block
                        pass 
                        self._state.following.append(self.FOLLOW_option_block_in_function_block_body232)
                        self.option_block()

                        self._state.following.pop()


                    else:
                        break #loop8






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "function_block_body"


    # $ANTLR start "fuzzify_block"
    # FCL.g:92:1: fuzzify_block : 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY' ;
    def fuzzify_block(self, ):

        variable_name3 = None


        try:
            try:
                # FCL.g:93:2: ( 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY' )
                # FCL.g:94:4: 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY'
                pass 
                self.match(self.input, 20, self.FOLLOW_20_in_fuzzify_block249)
                self._state.following.append(self.FOLLOW_variable_name_in_fuzzify_block255)
                variable_name3 = self.variable_name()

                self._state.following.pop()
                # FCL.g:96:4: ( linguistic_term[$variable_name.text] )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 28) :
                        alt9 = 1


                    if alt9 == 1:
                        # FCL.g:96:4: linguistic_term[$variable_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_fuzzify_block260)
                        self.linguistic_term(((variable_name3 is not None) and [self.input.toString(variable_name3.start,variable_name3.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop9


                self.match(self.input, 21, self.FOLLOW_21_in_fuzzify_block267)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "fuzzify_block"


    # $ANTLR start "defuzzify_block"
    # FCL.g:100:1: defuzzify_block : 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY' ;
    def defuzzify_block(self, ):

        f_variable_name4 = None


        try:
            try:
                # FCL.g:101:2: ( 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY' )
                # FCL.g:102:4: 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY'
                pass 
                self.match(self.input, 22, self.FOLLOW_22_in_defuzzify_block283)
                self._state.following.append(self.FOLLOW_f_variable_name_in_defuzzify_block289)
                f_variable_name4 = self.f_variable_name()

                self._state.following.pop()
                # FCL.g:104:4: ( linguistic_term[$f_variable_name.text] )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 28) :
                        alt10 = 1


                    if alt10 == 1:
                        # FCL.g:104:4: linguistic_term[$f_variable_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_defuzzify_block294)
                        self.linguistic_term(((f_variable_name4 is not None) and [self.input.toString(f_variable_name4.start,f_variable_name4.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop10


                self._state.following.append(self.FOLLOW_accumulation_method_in_defuzzify_block301)
                self.accumulation_method()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_defuzzification_method_in_defuzzify_block306)
                self.defuzzification_method(((f_variable_name4 is not None) and [self.input.toString(f_variable_name4.start,f_variable_name4.stop)] or [None])[0])

                self._state.following.pop()
                # FCL.g:107:4: ( default_value[$f_variable_name.text] )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 39) :
                    alt11 = 1
                if alt11 == 1:
                    # FCL.g:107:4: default_value[$f_variable_name.text]
                    pass 
                    self._state.following.append(self.FOLLOW_default_value_in_defuzzify_block312)
                    self.default_value(((f_variable_name4 is not None) and [self.input.toString(f_variable_name4.start,f_variable_name4.stop)] or [None])[0])

                    self._state.following.pop()



                # FCL.g:108:4: ( range )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 41) :
                    alt12 = 1
                if alt12 == 1:
                    # FCL.g:108:4: range
                    pass 
                    self._state.following.append(self.FOLLOW_range_in_defuzzify_block319)
                    self.range()

                    self._state.following.pop()



                self.match(self.input, 23, self.FOLLOW_23_in_defuzzify_block325)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "defuzzify_block"


    # $ANTLR start "rule_block"
    # FCL.g:112:1: rule_block : 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK' ;
    def rule_block(self, ):

        rule_block_name5 = None


        try:
            try:
                # FCL.g:113:2: ( 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK' )
                # FCL.g:114:4: 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK'
                pass 
                self.match(self.input, 24, self.FOLLOW_24_in_rule_block342)
                self._state.following.append(self.FOLLOW_rule_block_name_in_rule_block349)
                rule_block_name5 = self.rule_block_name()

                self._state.following.pop()
                # FCL.g:116:5: ( operator_definition )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 43 or LA13_0 == 47) :
                        alt13 = 1


                    if alt13 == 1:
                        # FCL.g:116:5: operator_definition
                        pass 
                        self._state.following.append(self.FOLLOW_operator_definition_in_rule_block355)
                        self.operator_definition()

                        self._state.following.pop()


                    else:
                        break #loop13


                # FCL.g:117:5: ( activation_method )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 51) :
                    alt14 = 1
                if alt14 == 1:
                    # FCL.g:117:5: activation_method
                    pass 
                    self._state.following.append(self.FOLLOW_activation_method_in_rule_block362)
                    self.activation_method()

                    self._state.following.pop()



                # FCL.g:118:5: ( rule[$rule_block_name.text] )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 58) :
                        alt15 = 1


                    if alt15 == 1:
                        # FCL.g:118:5: rule[$rule_block_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_rule_in_rule_block369)
                        self.rule(((rule_block_name5 is not None) and [self.input.toString(rule_block_name5.start,rule_block_name5.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop15


                self.match(self.input, 25, self.FOLLOW_25_in_rule_block376)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rule_block"


    # $ANTLR start "option_block"
    # FCL.g:121:1: option_block : 'OPTION' 'END_OPTION' ;
    def option_block(self, ):

        try:
            try:
                # FCL.g:121:14: ( 'OPTION' 'END_OPTION' )
                # FCL.g:121:16: 'OPTION' 'END_OPTION'
                pass 
                self.match(self.input, 26, self.FOLLOW_26_in_option_block384)
                self.match(self.input, 27, self.FOLLOW_27_in_option_block388)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "option_block"


    # $ANTLR start "linguistic_term"
    # FCL.g:125:1: linguistic_term[var_name] : 'TERM' term_name ':=' membership_function ';' ;
    def linguistic_term(self, var_name):

        term_name6 = None

        membership_function7 = None


        try:
            try:
                # FCL.g:126:2: ( 'TERM' term_name ':=' membership_function ';' )
                # FCL.g:127:2: 'TERM' term_name ':=' membership_function ';'
                pass 
                self.match(self.input, 28, self.FOLLOW_28_in_linguistic_term401)
                self._state.following.append(self.FOLLOW_term_name_in_linguistic_term403)
                term_name6 = self.term_name()

                self._state.following.pop()
                self.match(self.input, 29, self.FOLLOW_29_in_linguistic_term405)
                self._state.following.append(self.FOLLOW_membership_function_in_linguistic_term407)
                membership_function7 = self.membership_function()

                self._state.following.pop()
                self.match(self.input, 18, self.FOLLOW_18_in_linguistic_term409)
                #action start
                 
                self.System.variables[var_name].adjectives[((term_name6 is not None) and [self.input.toString(term_name6.start,term_name6.stop)] or [None])[0]]=fuzzy.Adjective.Adjective(membership_function7);

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "linguistic_term"


    # $ANTLR start "membership_function"
    # FCL.g:133:1: membership_function returns [set] : ( singleton | points );
    def membership_function(self, ):

        set = None

        singleton8 = None

        points9 = None


        try:
            try:
                # FCL.g:134:2: ( singleton | points )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((Identifier <= LA16_0 <= Real_literal)) :
                    alt16 = 1
                elif (LA16_0 == 18 or LA16_0 == 30) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # FCL.g:135:3: singleton
                    pass 
                    self._state.following.append(self.FOLLOW_singleton_in_membership_function429)
                    singleton8 = self.singleton()

                    self._state.following.pop()
                    #action start
                    set =  singleton8
                    #action end


                elif alt16 == 2:
                    # FCL.g:137:3: points
                    pass 
                    self._state.following.append(self.FOLLOW_points_in_membership_function440)
                    points9 = self.points()

                    self._state.following.pop()
                    #action start
                    set =  points9
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "membership_function"


    # $ANTLR start "singleton"
    # FCL.g:140:1: singleton returns [set] : ( numeric_literal | variable_name );
    def singleton(self, ):

        set = None

        numeric_literal10 = None


        try:
            try:
                # FCL.g:141:2: ( numeric_literal | variable_name )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((Integer_literal <= LA17_0 <= Real_literal)) :
                    alt17 = 1
                elif (LA17_0 == Identifier) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # FCL.g:142:3: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_singleton461)
                    numeric_literal10 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    set =  fuzzy.set.Singleton.Singleton(float(((numeric_literal10 is not None) and [self.input.toString(numeric_literal10.start,numeric_literal10.stop)] or [None])[0]))
                    #action end


                elif alt17 == 2:
                    # FCL.g:144:3: variable_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_singleton472)
                    self.variable_name()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "singleton"


    # $ANTLR start "points"
    # FCL.g:147:1: points returns [set] : ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* ;
    def points(self, ):

        set = None

        x = None

        y = None


               
        p=[]

        try:
            try:
                # FCL.g:151:2: ( ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* )
                # FCL.g:152:3: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                pass 
                # FCL.g:152:3: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == 30) :
                        alt19 = 1


                    if alt19 == 1:
                        # FCL.g:153:4: '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')'
                        pass 
                        self.match(self.input, 30, self.FOLLOW_30_in_points499)
                        # FCL.g:154:4: (x= numeric_literal | variable_name )
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if ((Integer_literal <= LA18_0 <= Real_literal)) :
                            alt18 = 1
                        elif (LA18_0 == Identifier) :
                            alt18 = 2
                        else:
                            nvae = NoViableAltException("", 18, 0, self.input)

                            raise nvae

                        if alt18 == 1:
                            # FCL.g:154:5: x= numeric_literal
                            pass 
                            self._state.following.append(self.FOLLOW_numeric_literal_in_points508)
                            x = self.numeric_literal()

                            self._state.following.pop()


                        elif alt18 == 2:
                            # FCL.g:154:25: variable_name
                            pass 
                            self._state.following.append(self.FOLLOW_variable_name_in_points512)
                            self.variable_name()

                            self._state.following.pop()



                        self.match(self.input, 31, self.FOLLOW_31_in_points519)
                        self._state.following.append(self.FOLLOW_numeric_literal_in_points527)
                        y = self.numeric_literal()

                        self._state.following.pop()
                        self.match(self.input, 32, self.FOLLOW_32_in_points533)
                        #action start
                        p.append((float(((x is not None) and [self.input.toString(x.start,x.stop)] or [None])[0]),float(((y is not None) and [self.input.toString(y.start,y.stop)] or [None])[0])));
                        #action end


                    else:
                        break #loop19


                #action start
                set =  fuzzy.set.Polygon.Polygon(p)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "points"


    # $ANTLR start "defuzzification_method"
    # FCL.g:163:1: defuzzification_method[var_name] : 'METHOD' ':' ( 'COG' | 'COGS' | 'COA' | 'LM' | 'RM' ) ';' ;
    def defuzzification_method(self, var_name):

        try:
            try:
                # FCL.g:163:35: ( 'METHOD' ':' ( 'COG' | 'COGS' | 'COA' | 'LM' | 'RM' ) ';' )
                # FCL.g:164:2: 'METHOD' ':' ( 'COG' | 'COGS' | 'COA' | 'LM' | 'RM' ) ';'
                pass 
                self.match(self.input, 33, self.FOLLOW_33_in_defuzzification_method566)
                self.match(self.input, 17, self.FOLLOW_17_in_defuzzification_method568)
                # FCL.g:165:2: ( 'COG' | 'COGS' | 'COA' | 'LM' | 'RM' )
                alt20 = 5
                LA20 = self.input.LA(1)
                if LA20 == 34:
                    alt20 = 1
                elif LA20 == 35:
                    alt20 = 2
                elif LA20 == 36:
                    alt20 = 3
                elif LA20 == 37:
                    alt20 = 4
                elif LA20 == 38:
                    alt20 = 5
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # FCL.g:165:3: 'COG'
                    pass 
                    self.match(self.input, 34, self.FOLLOW_34_in_defuzzification_method573)
                    #action start
                    self.System.variables[var_name].defuzzy = fuzzy.defuzzify.COG.COG();
                    #action end


                elif alt20 == 2:
                    # FCL.g:166:4: 'COGS'
                    pass 
                    self.match(self.input, 35, self.FOLLOW_35_in_defuzzification_method580)
                    #action start
                    self.System.variables[var_name].defuzzy = fuzzy.defuzzify.COGS.COGS();
                    #action end


                elif alt20 == 3:
                    # FCL.g:167:4: 'COA'
                    pass 
                    self.match(self.input, 36, self.FOLLOW_36_in_defuzzification_method587)


                elif alt20 == 4:
                    # FCL.g:168:4: 'LM'
                    pass 
                    self.match(self.input, 37, self.FOLLOW_37_in_defuzzification_method593)
                    #action start
                    self.System.variables[var_name].defuzzy = fuzzy.defuzzify.MaxLeft.MaxLeft();
                    #action end


                elif alt20 == 5:
                    # FCL.g:169:4: 'RM'
                    pass 
                    self.match(self.input, 38, self.FOLLOW_38_in_defuzzification_method600)
                    #action start
                    self.System.variables[var_name].defuzzy = fuzzy.defuzzify.MaxRight.MaxRight();
                    #action end



                self.match(self.input, 18, self.FOLLOW_18_in_defuzzification_method608)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "defuzzification_method"


    # $ANTLR start "default_value"
    # FCL.g:174:1: default_value[var_name] : 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';' ;
    def default_value(self, var_name):

        numeric_literal11 = None


        try:
            try:
                # FCL.g:174:26: ( 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';' )
                # FCL.g:175:2: 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';'
                pass 
                self.match(self.input, 39, self.FOLLOW_39_in_default_value622)
                self.match(self.input, 29, self.FOLLOW_29_in_default_value624)
                # FCL.g:176:2: ( numeric_literal | 'NC' )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((Integer_literal <= LA21_0 <= Real_literal)) :
                    alt21 = 1
                elif (LA21_0 == 40) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # FCL.g:177:3: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_default_value632)
                    numeric_literal11 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    self.System.variables[var_name].defuzzy.failsafe = float(((numeric_literal11 is not None) and [self.input.toString(numeric_literal11.start,numeric_literal11.stop)] or [None])[0]);
                    #action end


                elif alt21 == 2:
                    # FCL.g:179:3: 'NC'
                    pass 
                    self.match(self.input, 40, self.FOLLOW_40_in_default_value642)
                    #action start
                    self.System.variables[var_name].defuzzy.failsafe = None;
                    #action end



                self.match(self.input, 18, self.FOLLOW_18_in_default_value651)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "default_value"


    # $ANTLR start "range"
    # FCL.g:184:1: range : 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';' ;
    def range(self, ):

        try:
            try:
                # FCL.g:184:7: ( 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';' )
                # FCL.g:184:9: 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';'
                pass 
                self.match(self.input, 41, self.FOLLOW_41_in_range661)
                self.match(self.input, 29, self.FOLLOW_29_in_range663)
                self.match(self.input, 30, self.FOLLOW_30_in_range665)
                self._state.following.append(self.FOLLOW_numeric_literal_in_range667)
                self.numeric_literal()

                self._state.following.pop()
                self.match(self.input, 42, self.FOLLOW_42_in_range669)
                self._state.following.append(self.FOLLOW_numeric_literal_in_range671)
                self.numeric_literal()

                self._state.following.pop()
                self.match(self.input, 32, self.FOLLOW_32_in_range673)
                self.match(self.input, 18, self.FOLLOW_18_in_range675)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "range"


    # $ANTLR start "operator_definition"
    # FCL.g:186:1: operator_definition : ( ( 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' ) ) | ( 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' ) ) ) ';' ;
    def operator_definition(self, ):

        try:
            try:
                # FCL.g:186:21: ( ( ( 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' ) ) | ( 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' ) ) ) ';' )
                # FCL.g:186:23: ( ( 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' ) ) | ( 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' ) ) ) ';'
                pass 
                # FCL.g:186:23: ( ( 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' ) ) | ( 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' ) ) )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 43) :
                    alt22 = 1
                elif (LA22_0 == 47) :
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # FCL.g:186:24: ( 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' ) )
                    pass 
                    # FCL.g:186:24: ( 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' ) )
                    # FCL.g:186:25: 'OR' ':' ( 'MAX' | 'ASUM' | 'BSUM' )
                    pass 
                    self.match(self.input, 43, self.FOLLOW_43_in_operator_definition685)
                    self.match(self.input, 17, self.FOLLOW_17_in_operator_definition687)
                    if (44 <= self.input.LA(1) <= 46):
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse







                elif alt22 == 2:
                    # FCL.g:187:1: ( 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' ) )
                    pass 
                    # FCL.g:187:1: ( 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' ) )
                    # FCL.g:187:2: 'AND' ':' ( 'MIN' | 'PROD' | 'BDIF' )
                    pass 
                    self.match(self.input, 47, self.FOLLOW_47_in_operator_definition705)
                    self.match(self.input, 17, self.FOLLOW_17_in_operator_definition707)
                    if (48 <= self.input.LA(1) <= 50):
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse








                self.match(self.input, 18, self.FOLLOW_18_in_operator_definition723)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "operator_definition"


    # $ANTLR start "activation_method"
    # FCL.g:189:1: activation_method : 'ACT' ':' ( 'PROD' | 'MIN' ) ';' ;
    def activation_method(self, ):

        try:
            try:
                # FCL.g:189:19: ( 'ACT' ':' ( 'PROD' | 'MIN' ) ';' )
                # FCL.g:189:21: 'ACT' ':' ( 'PROD' | 'MIN' ) ';'
                pass 
                self.match(self.input, 51, self.FOLLOW_51_in_activation_method731)
                self.match(self.input, 17, self.FOLLOW_17_in_activation_method733)
                if (48 <= self.input.LA(1) <= 49):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self.match(self.input, 18, self.FOLLOW_18_in_activation_method743)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "activation_method"


    # $ANTLR start "accumulation_method"
    # FCL.g:191:1: accumulation_method : 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';' ;
    def accumulation_method(self, ):

        try:
            try:
                # FCL.g:191:21: ( 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';' )
                # FCL.g:191:23: 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';'
                pass 
                self.match(self.input, 52, self.FOLLOW_52_in_accumulation_method751)
                self.match(self.input, 17, self.FOLLOW_17_in_accumulation_method753)
                if self.input.LA(1) == 44 or self.input.LA(1) == 46 or self.input.LA(1) == 53:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self.match(self.input, 18, self.FOLLOW_18_in_accumulation_method767)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "accumulation_method"


    # $ANTLR start "condition"
    # FCL.g:193:1: condition returns [input] : (s1= subcondition | variable_name ) ( ( 'AND' (s2= subcondition | variable_name ) )+ | ( 'OR' (s3= subcondition | variable_name ) )+ )? ;
    def condition(self, ):

        input = None

        s1 = None

        s2 = None

        s3 = None


        try:
            try:
                # FCL.g:194:2: ( (s1= subcondition | variable_name ) ( ( 'AND' (s2= subcondition | variable_name ) )+ | ( 'OR' (s3= subcondition | variable_name ) )+ )? )
                # FCL.g:194:4: (s1= subcondition | variable_name ) ( ( 'AND' (s2= subcondition | variable_name ) )+ | ( 'OR' (s3= subcondition | variable_name ) )+ )?
                pass 
                # FCL.g:194:4: (s1= subcondition | variable_name )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 30 or LA23_0 == 54) :
                    alt23 = 1
                elif (LA23_0 == Identifier) :
                    LA23_2 = self.input.LA(2)

                    if (LA23_2 == 30 or (55 <= LA23_2 <= 56)) :
                        alt23 = 1
                    elif ((31 <= LA23_2 <= 32) or LA23_2 == 43 or LA23_2 == 47 or LA23_2 == 60) :
                        alt23 = 2
                    else:
                        nvae = NoViableAltException("", 23, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # FCL.g:194:5: s1= subcondition
                    pass 
                    self._state.following.append(self.FOLLOW_subcondition_in_condition783)
                    s1 = self.subcondition()

                    self._state.following.pop()
                    #action start
                    input = s1
                    #action end


                elif alt23 == 2:
                    # FCL.g:194:43: variable_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_condition788)
                    self.variable_name()

                    self._state.following.pop()



                # FCL.g:195:3: ( ( 'AND' (s2= subcondition | variable_name ) )+ | ( 'OR' (s3= subcondition | variable_name ) )+ )?
                alt28 = 3
                LA28_0 = self.input.LA(1)

                if (LA28_0 == 47) :
                    alt28 = 1
                elif (LA28_0 == 43) :
                    alt28 = 2
                if alt28 == 1:
                    # FCL.g:196:4: ( 'AND' (s2= subcondition | variable_name ) )+
                    pass 
                    # FCL.g:196:4: ( 'AND' (s2= subcondition | variable_name ) )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == 47) :
                            alt25 = 1


                        if alt25 == 1:
                            # FCL.g:196:5: 'AND' (s2= subcondition | variable_name )
                            pass 
                            self.match(self.input, 47, self.FOLLOW_47_in_condition800)
                            # FCL.g:196:11: (s2= subcondition | variable_name )
                            alt24 = 2
                            LA24_0 = self.input.LA(1)

                            if (LA24_0 == 30 or LA24_0 == 54) :
                                alt24 = 1
                            elif (LA24_0 == Identifier) :
                                LA24_2 = self.input.LA(2)

                                if (LA24_2 == 30 or (55 <= LA24_2 <= 56)) :
                                    alt24 = 1
                                elif ((31 <= LA24_2 <= 32) or LA24_2 == 47 or LA24_2 == 60) :
                                    alt24 = 2
                                else:
                                    nvae = NoViableAltException("", 24, 2, self.input)

                                    raise nvae

                            else:
                                nvae = NoViableAltException("", 24, 0, self.input)

                                raise nvae

                            if alt24 == 1:
                                # FCL.g:196:12: s2= subcondition
                                pass 
                                self._state.following.append(self.FOLLOW_subcondition_in_condition805)
                                s2 = self.subcondition()

                                self._state.following.pop()
                                #action start
                                input =  fuzzy.operator.Compound.Compound(fuzzy.norm.Min.Min(),input,s2)
                                #action end


                            elif alt24 == 2:
                                # FCL.g:196:114: variable_name
                                pass 
                                self._state.following.append(self.FOLLOW_variable_name_in_condition811)
                                self.variable_name()

                                self._state.following.pop()





                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1




                elif alt28 == 2:
                    # FCL.g:198:4: ( 'OR' (s3= subcondition | variable_name ) )+
                    pass 
                    # FCL.g:198:4: ( 'OR' (s3= subcondition | variable_name ) )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == 43) :
                            alt27 = 1


                        if alt27 == 1:
                            # FCL.g:198:5: 'OR' (s3= subcondition | variable_name )
                            pass 
                            self.match(self.input, 43, self.FOLLOW_43_in_condition824)
                            # FCL.g:198:10: (s3= subcondition | variable_name )
                            alt26 = 2
                            LA26_0 = self.input.LA(1)

                            if (LA26_0 == 30 or LA26_0 == 54) :
                                alt26 = 1
                            elif (LA26_0 == Identifier) :
                                LA26_2 = self.input.LA(2)

                                if (LA26_2 == 30 or (55 <= LA26_2 <= 56)) :
                                    alt26 = 1
                                elif ((31 <= LA26_2 <= 32) or LA26_2 == 43 or LA26_2 == 60) :
                                    alt26 = 2
                                else:
                                    nvae = NoViableAltException("", 26, 2, self.input)

                                    raise nvae

                            else:
                                nvae = NoViableAltException("", 26, 0, self.input)

                                raise nvae

                            if alt26 == 1:
                                # FCL.g:198:11: s3= subcondition
                                pass 
                                self._state.following.append(self.FOLLOW_subcondition_in_condition829)
                                s3 = self.subcondition()

                                self._state.following.pop()
                                #action start
                                input =  fuzzy.operator.Compound.Compound(fuzzy.norm.Min.Min(),input,s3)
                                #action end


                            elif alt26 == 2:
                                # FCL.g:198:113: variable_name
                                pass 
                                self._state.following.append(self.FOLLOW_variable_name_in_condition835)
                                self.variable_name()

                                self._state.following.pop()





                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1









            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "condition"


    # $ANTLR start "subcondition"
    # FCL.g:202:1: subcondition returns [input] : ( ( 'NOT' '(' subcondition2 ')' ) | ( subcondition2 ) );
    def subcondition(self, ):

        input = None

        subcondition212 = None

        subcondition213 = None


        try:
            try:
                # FCL.g:203:2: ( ( 'NOT' '(' subcondition2 ')' ) | ( subcondition2 ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 54) :
                    alt29 = 1
                elif (LA29_0 == Identifier or LA29_0 == 30) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # FCL.g:203:4: ( 'NOT' '(' subcondition2 ')' )
                    pass 
                    # FCL.g:203:4: ( 'NOT' '(' subcondition2 ')' )
                    # FCL.g:203:5: 'NOT' '(' subcondition2 ')'
                    pass 
                    self.match(self.input, 54, self.FOLLOW_54_in_subcondition859)
                    self.match(self.input, 30, self.FOLLOW_30_in_subcondition861)
                    self._state.following.append(self.FOLLOW_subcondition2_in_subcondition863)
                    subcondition212 = self.subcondition2()

                    self._state.following.pop()
                    self.match(self.input, 32, self.FOLLOW_32_in_subcondition865)
                    #action start
                    input =  fuzzy.operator.Not.Not(subcondition212)
                    #action end





                elif alt29 == 2:
                    # FCL.g:204:4: ( subcondition2 )
                    pass 
                    # FCL.g:204:4: ( subcondition2 )
                    # FCL.g:204:6: subcondition2
                    pass 
                    self._state.following.append(self.FOLLOW_subcondition2_in_subcondition876)
                    subcondition213 = self.subcondition2()

                    self._state.following.pop()
                    #action start
                    input =  subcondition213
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "subcondition"


    # $ANTLR start "subcondition2"
    # FCL.g:207:1: subcondition2 returns [input] : ( ( '(' c1= condition ')' ) | ( variable_name 'IS' (x= 'NOT' )? term_name ) | i1= Identifier ( '[' param= numeric_literal ']' )? '(' c4= condition ',' c5= condition ')' );
    def subcondition2(self, ):

        input = None

        x = None
        i1 = None
        c1 = None

        param = None

        c4 = None

        c5 = None

        variable_name14 = None

        term_name15 = None


        try:
            try:
                # FCL.g:208:2: ( ( '(' c1= condition ')' ) | ( variable_name 'IS' (x= 'NOT' )? term_name ) | i1= Identifier ( '[' param= numeric_literal ']' )? '(' c4= condition ',' c5= condition ')' )
                alt32 = 3
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 30) :
                    alt32 = 1
                elif (LA32_0 == Identifier) :
                    LA32_2 = self.input.LA(2)

                    if (LA32_2 == 30 or LA32_2 == 56) :
                        alt32 = 3
                    elif (LA32_2 == 55) :
                        alt32 = 2
                    else:
                        nvae = NoViableAltException("", 32, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # FCL.g:208:4: ( '(' c1= condition ')' )
                    pass 
                    # FCL.g:208:4: ( '(' c1= condition ')' )
                    # FCL.g:208:5: '(' c1= condition ')'
                    pass 
                    self.match(self.input, 30, self.FOLLOW_30_in_subcondition2895)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition2899)
                    c1 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 32, self.FOLLOW_32_in_subcondition2901)
                    #action start
                    input =  c1
                    #action end





                elif alt32 == 2:
                    # FCL.g:209:4: ( variable_name 'IS' (x= 'NOT' )? term_name )
                    pass 
                    # FCL.g:209:4: ( variable_name 'IS' (x= 'NOT' )? term_name )
                    # FCL.g:209:6: variable_name 'IS' (x= 'NOT' )? term_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_subcondition2912)
                    variable_name14 = self.variable_name()

                    self._state.following.pop()
                    self.match(self.input, 55, self.FOLLOW_55_in_subcondition2914)
                    # FCL.g:209:26: (x= 'NOT' )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 54) :
                        alt30 = 1
                    if alt30 == 1:
                        # FCL.g:209:26: x= 'NOT'
                        pass 
                        x=self.match(self.input, 54, self.FOLLOW_54_in_subcondition2918)



                    self._state.following.append(self.FOLLOW_term_name_in_subcondition2921)
                    term_name15 = self.term_name()

                    self._state.following.pop()
                    #action start
                                                                
                    input = fuzzy.operator.Input.Input(self.System.variables[((variable_name14 is not None) and [self.input.toString(variable_name14.start,variable_name14.stop)] or [None])[0]].adjectives[((term_name15 is not None) and [self.input.toString(term_name15.start,term_name15.stop)] or [None])[0]])
                    if x is not None:
                    	input = fuzzy.operator.Not.Not(input)

                    #action end





                elif alt32 == 3:
                    # FCL.g:214:4: i1= Identifier ( '[' param= numeric_literal ']' )? '(' c4= condition ',' c5= condition ')'
                    pass 
                    i1=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_subcondition2931)
                    # FCL.g:214:18: ( '[' param= numeric_literal ']' )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == 56) :
                        alt31 = 1
                    if alt31 == 1:
                        # FCL.g:214:19: '[' param= numeric_literal ']'
                        pass 
                        self.match(self.input, 56, self.FOLLOW_56_in_subcondition2934)
                        self._state.following.append(self.FOLLOW_numeric_literal_in_subcondition2938)
                        param = self.numeric_literal()

                        self._state.following.pop()
                        self.match(self.input, 57, self.FOLLOW_57_in_subcondition2940)



                    self.match(self.input, 30, self.FOLLOW_30_in_subcondition2944)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition2948)
                    c4 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 31, self.FOLLOW_31_in_subcondition2950)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition2954)
                    c5 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 32, self.FOLLOW_32_in_subcondition2956)
                    #action start
                                                                                                             
                    if ((param is not None) and [self.input.toString(param.start,param.stop)] or [None])[0] is not None:
                    	p = float(((param is not None) and [self.input.toString(param.start,param.stop)] or [None])[0])
                    else:
                    	p = None
                    input =  fuzzy.operator.Compound.Compound(getNorm(i1.text,p),c4,c5)
                    	
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "subcondition2"


    # $ANTLR start "conclusion"
    # FCL.g:223:1: conclusion returns [adj] : ( conclusion2 ',' )* c2= conclusion2 ;
    def conclusion(self, ):

        adj = None

        c2 = None


        try:
            try:
                # FCL.g:224:2: ( ( conclusion2 ',' )* c2= conclusion2 )
                # FCL.g:224:4: ( conclusion2 ',' )* c2= conclusion2
                pass 
                # FCL.g:224:4: ( conclusion2 ',' )*
                while True: #loop33
                    alt33 = 2
                    alt33 = self.dfa33.predict(self.input)
                    if alt33 == 1:
                        # FCL.g:224:6: conclusion2 ','
                        pass 
                        self._state.following.append(self.FOLLOW_conclusion2_in_conclusion976)
                        self.conclusion2()

                        self._state.following.pop()
                        self.match(self.input, 31, self.FOLLOW_31_in_conclusion978)


                    else:
                        break #loop33


                self._state.following.append(self.FOLLOW_conclusion2_in_conclusion986)
                c2 = self.conclusion2()

                self._state.following.pop()
                #action start
                adj = c2
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion"


    # $ANTLR start "conclusion2"
    # FCL.g:228:1: conclusion2 returns [adj] : ( ( '(' c2= conclusion3 ')' ) | (c1= conclusion3 ) );
    def conclusion2(self, ):

        adj = None

        c2 = None

        c1 = None


        try:
            try:
                # FCL.g:229:2: ( ( '(' c2= conclusion3 ')' ) | (c1= conclusion3 ) )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 30) :
                    alt34 = 1
                elif (LA34_0 == Identifier) :
                    alt34 = 2
                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # FCL.g:229:4: ( '(' c2= conclusion3 ')' )
                    pass 
                    # FCL.g:229:4: ( '(' c2= conclusion3 ')' )
                    # FCL.g:230:3: '(' c2= conclusion3 ')'
                    pass 
                    self.match(self.input, 30, self.FOLLOW_30_in_conclusion21008)
                    self._state.following.append(self.FOLLOW_conclusion3_in_conclusion21012)
                    c2 = self.conclusion3()

                    self._state.following.pop()
                    self.match(self.input, 32, self.FOLLOW_32_in_conclusion21015)
                    #action start
                    adj = c2
                    #action end





                elif alt34 == 2:
                    # FCL.g:231:4: (c1= conclusion3 )
                    pass 
                    # FCL.g:231:4: (c1= conclusion3 )
                    # FCL.g:231:10: c1= conclusion3
                    pass 
                    self._state.following.append(self.FOLLOW_conclusion3_in_conclusion21032)
                    c1 = self.conclusion3()

                    self._state.following.pop()
                    #action start
                    adj = c1
                    #action end






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion2"


    # $ANTLR start "conclusion3"
    # FCL.g:234:1: conclusion3 returns [adj] : ( variable_name | (v2= variable_name 'IS' t2= term_name ) ) ;
    def conclusion3(self, ):

        adj = None

        v2 = None

        t2 = None


        try:
            try:
                # FCL.g:235:2: ( ( variable_name | (v2= variable_name 'IS' t2= term_name ) ) )
                # FCL.g:235:4: ( variable_name | (v2= variable_name 'IS' t2= term_name ) )
                pass 
                # FCL.g:235:4: ( variable_name | (v2= variable_name 'IS' t2= term_name ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == Identifier) :
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == 55) :
                        alt35 = 2
                    elif (LA35_1 == 18 or (31 <= LA35_1 <= 32) or LA35_1 == 61) :
                        alt35 = 1
                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # FCL.g:235:5: variable_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_conclusion31057)
                    self.variable_name()

                    self._state.following.pop()


                elif alt35 == 2:
                    # FCL.g:235:21: (v2= variable_name 'IS' t2= term_name )
                    pass 
                    # FCL.g:235:21: (v2= variable_name 'IS' t2= term_name )
                    # FCL.g:235:22: v2= variable_name 'IS' t2= term_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_conclusion31064)
                    v2 = self.variable_name()

                    self._state.following.pop()
                    self.match(self.input, 55, self.FOLLOW_55_in_conclusion31066)
                    self._state.following.append(self.FOLLOW_term_name_in_conclusion31070)
                    t2 = self.term_name()

                    self._state.following.pop()
                    #action start
                    adj = self.System.variables[((v2 is not None) and [self.input.toString(v2.start,v2.stop)] or [None])[0]].adjectives[((t2 is not None) and [self.input.toString(t2.start,t2.stop)] or [None])[0]]
                    #action end










            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion3"


    # $ANTLR start "rule"
    # FCL.g:239:1: rule[block_name] : 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';' ;
    def rule(self, block_name):

        Integer_literal19 = None
        weighting_factor16 = None

        condition17 = None

        conclusion18 = None


              
        certainty = 1.0

        try:
            try:
                # FCL.g:242:3: ( 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';' )
                # FCL.g:242:5: 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';'
                pass 
                self.match(self.input, 58, self.FOLLOW_58_in_rule1091)
                Integer_literal19=self.match(self.input, Integer_literal, self.FOLLOW_Integer_literal_in_rule1093)
                self.match(self.input, 17, self.FOLLOW_17_in_rule1095)
                self.match(self.input, 59, self.FOLLOW_59_in_rule1097)
                self._state.following.append(self.FOLLOW_condition_in_rule1099)
                condition17 = self.condition()

                self._state.following.pop()
                self.match(self.input, 60, self.FOLLOW_60_in_rule1101)
                self._state.following.append(self.FOLLOW_conclusion_in_rule1103)
                conclusion18 = self.conclusion()

                self._state.following.pop()
                # FCL.g:242:65: ( 'WITH' weighting_factor )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == 61) :
                    alt36 = 1
                if alt36 == 1:
                    # FCL.g:242:66: 'WITH' weighting_factor
                    pass 
                    self.match(self.input, 61, self.FOLLOW_61_in_rule1106)
                    self._state.following.append(self.FOLLOW_weighting_factor_in_rule1108)
                    weighting_factor16 = self.weighting_factor()

                    self._state.following.pop()
                    #action start
                    certainty = float(((weighting_factor16 is not None) and [self.input.toString(weighting_factor16.start,weighting_factor16.stop)] or [None])[0]);
                    #action end



                self.match(self.input, 18, self.FOLLOW_18_in_rule1114)
                #action start
                 
                input = condition17
                adjective = conclusion18
                self.System.rules[block_name+'.'+Integer_literal19.text] = fuzzy.Rule.Rule(adjective,input,certainty=certainty)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rule"

    class weighting_factor_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "weighting_factor"
    # FCL.g:250:1: weighting_factor : ( variable | numeric_literal );
    def weighting_factor(self, ):

        retval = self.weighting_factor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:250:18: ( variable | numeric_literal )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == Identifier) :
                    alt37 = 1
                elif ((Integer_literal <= LA37_0 <= Real_literal)) :
                    alt37 = 2
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae

                if alt37 == 1:
                    # FCL.g:250:20: variable
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_weighting_factor1125)
                    self.variable()

                    self._state.following.pop()


                elif alt37 == 2:
                    # FCL.g:250:31: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_weighting_factor1129)
                    self.numeric_literal()

                    self._state.following.pop()


                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "weighting_factor"

    class function_block_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "function_block_name"
    # FCL.g:252:1: function_block_name : Identifier ;
    def function_block_name(self, ):

        retval = self.function_block_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:252:21: ( Identifier )
                # FCL.g:252:23: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_function_block_name1137)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "function_block_name"

    class rule_block_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "rule_block_name"
    # FCL.g:254:1: rule_block_name : Identifier ;
    def rule_block_name(self, ):

        retval = self.rule_block_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:254:17: ( Identifier )
                # FCL.g:254:19: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_rule_block_name1145)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "rule_block_name"

    class term_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "term_name"
    # FCL.g:255:1: term_name : Identifier ;
    def term_name(self, ):

        retval = self.term_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:255:11: ( Identifier )
                # FCL.g:255:13: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_term_name1153)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "term_name"

    class f_variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "f_variable_name"
    # FCL.g:256:1: f_variable_name : Identifier ;
    def f_variable_name(self, ):

        retval = self.f_variable_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:256:17: ( Identifier )
                # FCL.g:256:19: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_f_variable_name1161)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "f_variable_name"

    class variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "variable_name"
    # FCL.g:257:1: variable_name : Identifier ;
    def variable_name(self, ):

        retval = self.variable_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:257:15: ( Identifier )
                # FCL.g:257:17: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_variable_name1169)



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "variable_name"

    class numeric_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "numeric_literal"
    # FCL.g:258:1: numeric_literal : ( Integer_literal | Real_literal );
    def numeric_literal(self, ):

        retval = self.numeric_literal_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # FCL.g:258:17: ( Integer_literal | Real_literal )
                # FCL.g:
                pass 
                if (Integer_literal <= self.input.LA(1) <= Real_literal):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "numeric_literal"


    # $ANTLR start "variable"
    # FCL.g:260:1: variable : variable_name ;
    def variable(self, ):

        try:
            try:
                # FCL.g:261:2: ( variable_name )
                # FCL.g:261:5: variable_name
                pass 
                self._state.following.append(self.FOLLOW_variable_name_in_variable1192)
                self.variable_name()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "variable"


    # Delegated rules


    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\2\4\1\22\1\40\1\4\2\uffff\1\22\1\4\1\22\1\40"
        )

    DFA33_max = DFA.unpack(
        u"\1\36\1\4\1\75\1\67\1\4\2\uffff\1\75\1\4\1\75\1\40"
        )

    DFA33_accept = DFA.unpack(
        u"\5\uffff\1\1\1\2\4\uffff"
        )

    DFA33_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\1\2\31\uffff\1\1"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\6\14\uffff\1\5\27\uffff\1\4\5\uffff\1\6"),
        DFA.unpack(u"\1\7\26\uffff\1\10"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\14\uffff\1\5\35\uffff\1\6"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\6\14\uffff\1\5\35\uffff\1\6"),
        DFA.unpack(u"\1\7")
    ]

    # class definition for DFA #33

    DFA33 = DFA
 

    FOLLOW_function_block_declaration_in_main44 = frozenset([1])
    FOLLOW_12_in_function_block_declaration59 = frozenset([4])
    FOLLOW_function_block_name_in_function_block_declaration64 = frozenset([13, 14, 16, 20, 22, 24, 26])
    FOLLOW_fb_io_var_declarations_in_function_block_declaration70 = frozenset([13, 14, 16, 20, 22, 24, 26])
    FOLLOW_function_block_body_in_function_block_declaration78 = frozenset([13])
    FOLLOW_13_in_function_block_declaration82 = frozenset([])
    FOLLOW_EOF_in_function_block_declaration87 = frozenset([1])
    FOLLOW_input_declarations_in_fb_io_var_declarations99 = frozenset([1])
    FOLLOW_output_declarations_in_fb_io_var_declarations105 = frozenset([1])
    FOLLOW_14_in_input_declarations115 = frozenset([4])
    FOLLOW_var_decl_in_input_declarations117 = frozenset([4, 15])
    FOLLOW_15_in_input_declarations121 = frozenset([1])
    FOLLOW_16_in_output_declarations129 = frozenset([4])
    FOLLOW_var_decl_in_output_declarations131 = frozenset([4, 15])
    FOLLOW_15_in_output_declarations135 = frozenset([1])
    FOLLOW_Identifier_in_var_decl149 = frozenset([17])
    FOLLOW_17_in_var_decl154 = frozenset([19])
    FOLLOW_type_in_var_decl159 = frozenset([18])
    FOLLOW_18_in_var_decl164 = frozenset([1])
    FOLLOW_19_in_type178 = frozenset([1])
    FOLLOW_var_declarations_in_other_var_declarations189 = frozenset([1])
    FOLLOW_fuzzify_block_in_function_block_body211 = frozenset([1, 20, 22, 24, 26])
    FOLLOW_defuzzify_block_in_function_block_body217 = frozenset([1, 22, 24, 26])
    FOLLOW_rule_block_in_function_block_body226 = frozenset([1, 24, 26])
    FOLLOW_option_block_in_function_block_body232 = frozenset([1, 26])
    FOLLOW_20_in_fuzzify_block249 = frozenset([4])
    FOLLOW_variable_name_in_fuzzify_block255 = frozenset([21, 28])
    FOLLOW_linguistic_term_in_fuzzify_block260 = frozenset([21, 28])
    FOLLOW_21_in_fuzzify_block267 = frozenset([1])
    FOLLOW_22_in_defuzzify_block283 = frozenset([4])
    FOLLOW_f_variable_name_in_defuzzify_block289 = frozenset([28, 52])
    FOLLOW_linguistic_term_in_defuzzify_block294 = frozenset([28, 52])
    FOLLOW_accumulation_method_in_defuzzify_block301 = frozenset([33])
    FOLLOW_defuzzification_method_in_defuzzify_block306 = frozenset([23, 39, 41])
    FOLLOW_default_value_in_defuzzify_block312 = frozenset([23, 41])
    FOLLOW_range_in_defuzzify_block319 = frozenset([23])
    FOLLOW_23_in_defuzzify_block325 = frozenset([1])
    FOLLOW_24_in_rule_block342 = frozenset([4])
    FOLLOW_rule_block_name_in_rule_block349 = frozenset([25, 43, 47, 51, 58])
    FOLLOW_operator_definition_in_rule_block355 = frozenset([25, 43, 47, 51, 58])
    FOLLOW_activation_method_in_rule_block362 = frozenset([25, 58])
    FOLLOW_rule_in_rule_block369 = frozenset([25, 58])
    FOLLOW_25_in_rule_block376 = frozenset([1])
    FOLLOW_26_in_option_block384 = frozenset([27])
    FOLLOW_27_in_option_block388 = frozenset([1])
    FOLLOW_28_in_linguistic_term401 = frozenset([4])
    FOLLOW_term_name_in_linguistic_term403 = frozenset([29])
    FOLLOW_29_in_linguistic_term405 = frozenset([4, 5, 6, 30])
    FOLLOW_membership_function_in_linguistic_term407 = frozenset([18])
    FOLLOW_18_in_linguistic_term409 = frozenset([1])
    FOLLOW_singleton_in_membership_function429 = frozenset([1])
    FOLLOW_points_in_membership_function440 = frozenset([1])
    FOLLOW_numeric_literal_in_singleton461 = frozenset([1])
    FOLLOW_variable_name_in_singleton472 = frozenset([1])
    FOLLOW_30_in_points499 = frozenset([4, 5, 6])
    FOLLOW_numeric_literal_in_points508 = frozenset([31])
    FOLLOW_variable_name_in_points512 = frozenset([31])
    FOLLOW_31_in_points519 = frozenset([5, 6])
    FOLLOW_numeric_literal_in_points527 = frozenset([32])
    FOLLOW_32_in_points533 = frozenset([1, 30])
    FOLLOW_33_in_defuzzification_method566 = frozenset([17])
    FOLLOW_17_in_defuzzification_method568 = frozenset([34, 35, 36, 37, 38])
    FOLLOW_34_in_defuzzification_method573 = frozenset([18])
    FOLLOW_35_in_defuzzification_method580 = frozenset([18])
    FOLLOW_36_in_defuzzification_method587 = frozenset([18])
    FOLLOW_37_in_defuzzification_method593 = frozenset([18])
    FOLLOW_38_in_defuzzification_method600 = frozenset([18])
    FOLLOW_18_in_defuzzification_method608 = frozenset([1])
    FOLLOW_39_in_default_value622 = frozenset([29])
    FOLLOW_29_in_default_value624 = frozenset([5, 6, 40])
    FOLLOW_numeric_literal_in_default_value632 = frozenset([18])
    FOLLOW_40_in_default_value642 = frozenset([18])
    FOLLOW_18_in_default_value651 = frozenset([1])
    FOLLOW_41_in_range661 = frozenset([29])
    FOLLOW_29_in_range663 = frozenset([30])
    FOLLOW_30_in_range665 = frozenset([5, 6])
    FOLLOW_numeric_literal_in_range667 = frozenset([42])
    FOLLOW_42_in_range669 = frozenset([5, 6])
    FOLLOW_numeric_literal_in_range671 = frozenset([32])
    FOLLOW_32_in_range673 = frozenset([18])
    FOLLOW_18_in_range675 = frozenset([1])
    FOLLOW_43_in_operator_definition685 = frozenset([17])
    FOLLOW_17_in_operator_definition687 = frozenset([44, 45, 46])
    FOLLOW_set_in_operator_definition689 = frozenset([18])
    FOLLOW_47_in_operator_definition705 = frozenset([17])
    FOLLOW_17_in_operator_definition707 = frozenset([48, 49, 50])
    FOLLOW_set_in_operator_definition709 = frozenset([18])
    FOLLOW_18_in_operator_definition723 = frozenset([1])
    FOLLOW_51_in_activation_method731 = frozenset([17])
    FOLLOW_17_in_activation_method733 = frozenset([48, 49])
    FOLLOW_set_in_activation_method735 = frozenset([18])
    FOLLOW_18_in_activation_method743 = frozenset([1])
    FOLLOW_52_in_accumulation_method751 = frozenset([17])
    FOLLOW_17_in_accumulation_method753 = frozenset([44, 46, 53])
    FOLLOW_set_in_accumulation_method755 = frozenset([18])
    FOLLOW_18_in_accumulation_method767 = frozenset([1])
    FOLLOW_subcondition_in_condition783 = frozenset([1, 43, 47])
    FOLLOW_variable_name_in_condition788 = frozenset([1, 43, 47])
    FOLLOW_47_in_condition800 = frozenset([4, 30, 54])
    FOLLOW_subcondition_in_condition805 = frozenset([1, 47])
    FOLLOW_variable_name_in_condition811 = frozenset([1, 47])
    FOLLOW_43_in_condition824 = frozenset([4, 30, 54])
    FOLLOW_subcondition_in_condition829 = frozenset([1, 43])
    FOLLOW_variable_name_in_condition835 = frozenset([1, 43])
    FOLLOW_54_in_subcondition859 = frozenset([30])
    FOLLOW_30_in_subcondition861 = frozenset([4, 30, 54])
    FOLLOW_subcondition2_in_subcondition863 = frozenset([32])
    FOLLOW_32_in_subcondition865 = frozenset([1])
    FOLLOW_subcondition2_in_subcondition876 = frozenset([1])
    FOLLOW_30_in_subcondition2895 = frozenset([4, 30, 54])
    FOLLOW_condition_in_subcondition2899 = frozenset([32])
    FOLLOW_32_in_subcondition2901 = frozenset([1])
    FOLLOW_variable_name_in_subcondition2912 = frozenset([55])
    FOLLOW_55_in_subcondition2914 = frozenset([4, 54])
    FOLLOW_54_in_subcondition2918 = frozenset([4])
    FOLLOW_term_name_in_subcondition2921 = frozenset([1])
    FOLLOW_Identifier_in_subcondition2931 = frozenset([30, 56])
    FOLLOW_56_in_subcondition2934 = frozenset([5, 6])
    FOLLOW_numeric_literal_in_subcondition2938 = frozenset([57])
    FOLLOW_57_in_subcondition2940 = frozenset([30])
    FOLLOW_30_in_subcondition2944 = frozenset([4, 30, 54])
    FOLLOW_condition_in_subcondition2948 = frozenset([31])
    FOLLOW_31_in_subcondition2950 = frozenset([4, 30, 54])
    FOLLOW_condition_in_subcondition2954 = frozenset([32])
    FOLLOW_32_in_subcondition2956 = frozenset([1])
    FOLLOW_conclusion2_in_conclusion976 = frozenset([31])
    FOLLOW_31_in_conclusion978 = frozenset([4, 30])
    FOLLOW_conclusion2_in_conclusion986 = frozenset([1])
    FOLLOW_30_in_conclusion21008 = frozenset([4, 30])
    FOLLOW_conclusion3_in_conclusion21012 = frozenset([32])
    FOLLOW_32_in_conclusion21015 = frozenset([1])
    FOLLOW_conclusion3_in_conclusion21032 = frozenset([1])
    FOLLOW_variable_name_in_conclusion31057 = frozenset([1])
    FOLLOW_variable_name_in_conclusion31064 = frozenset([55])
    FOLLOW_55_in_conclusion31066 = frozenset([4])
    FOLLOW_term_name_in_conclusion31070 = frozenset([1])
    FOLLOW_58_in_rule1091 = frozenset([5])
    FOLLOW_Integer_literal_in_rule1093 = frozenset([17])
    FOLLOW_17_in_rule1095 = frozenset([59])
    FOLLOW_59_in_rule1097 = frozenset([4, 30, 54])
    FOLLOW_condition_in_rule1099 = frozenset([60])
    FOLLOW_60_in_rule1101 = frozenset([4, 30])
    FOLLOW_conclusion_in_rule1103 = frozenset([18, 61])
    FOLLOW_61_in_rule1106 = frozenset([4, 5, 6])
    FOLLOW_weighting_factor_in_rule1108 = frozenset([18])
    FOLLOW_18_in_rule1114 = frozenset([1])
    FOLLOW_variable_in_weighting_factor1125 = frozenset([1])
    FOLLOW_numeric_literal_in_weighting_factor1129 = frozenset([1])
    FOLLOW_Identifier_in_function_block_name1137 = frozenset([1])
    FOLLOW_Identifier_in_rule_block_name1145 = frozenset([1])
    FOLLOW_Identifier_in_term_name1153 = frozenset([1])
    FOLLOW_Identifier_in_f_variable_name1161 = frozenset([1])
    FOLLOW_Identifier_in_variable_name1169 = frozenset([1])
    FOLLOW_set_in_numeric_literal0 = frozenset([1])
    FOLLOW_variable_name_in_variable1192 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FCLLexer", FCLParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
