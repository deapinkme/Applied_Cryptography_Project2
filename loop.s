# A simple loop, counting down from 10

    movi $1,10         # Initialize counter to 10
beginning:
    jeq $1, $0,done     # if $1 == $0, go to done
    addi $1, $1,-1      # Decrement $1
    j beginning         # go to top of loop
done: halt                # we've finished

#--
#--
#--MACHINE CODE
# ram[0] = 16'b1110000010001010;		// movi $1,10
# ram[1] = 16'b1100010000000010;		// beginning: jeq $1,$0,done
# ram[2] = 16'b1110010011111111;		// addi $1,$1,-1
# ram[3] = 16'b0100000000000001;		// j beginning
# ram[4] = 16'b0100000000000100;		// done: halt 
#--
#--
#--EXECUTION OUTPUT
# Final state:
# 	pc=    4
# 	$0=    0
# 	$1=    0
# 	$2=    0
# 	$3=    0
# 	$4=    0
# 	$5=    0
# 	$6=    0
# 	$7=    0
# e08a c402 e4ff 4001 4004 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 