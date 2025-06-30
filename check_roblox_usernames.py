#include <std.h>

#define BASE    "ALT"   // Prefix
#define LENGTH  10      // Username length  
#define COUNT   30      // Number to generate  
#define DELAY   500     // Delay in ms  

U0 GenUsername(U8 *buf, U8 *base, I64 len)  
{
  I64 i, base_len = StrLen(base);  
  MemCpy(buf, base, base_len);  

  for (i = base_len; i < len; i++)  
    buf[i] = (Rand % 2) ? (Rand % 10 + '0') : (Rand % 26 + 'a');  
  buf[len] = 0;  
}  

BOOL CheckUsername(U8 *name)  
{
  // TempleOS can't do HTTPS, so this is a placeholder  
  "%s\n", name;  
  return Rand % 2; // Random result for demo  
}  

U0 Main()  
{
  U8 names[COUNT][LENGTH+1];  
  U8 available[COUNT][LENGTH+1];  
  I64 i, avail_count = 0;  

  for (i = 0; i < COUNT; i++)  
    GenUsername(names[i], BASE, LENGTH);  

  "Checking %d usernames...\n\n", COUNT;  
  for (i = 0; i < COUNT; i++)  
  {
    if (CheckUsername(names[i]))  
    {
      "AVAILABLE: %s\n", names[i];  
      StrCpy(available[avail_count++], names[i]);  
    }  
    else  
      "TAKEN: %s\n", names[i];  

    MSleep(DELAY);  
  }  

  "\nDone.\nAvailable: %d\n", avail_count;  
}
