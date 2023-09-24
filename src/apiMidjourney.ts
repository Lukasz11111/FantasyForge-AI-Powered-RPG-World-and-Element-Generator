import "dotenv/config";
import { Midjourney } from "midjourney";
import * as fs from 'fs';

const filePath: string = 'promptTmp.txt';

function readFileSync(filePath: string): string {
  try {
    const fileContents: string = fs.readFileSync(filePath, 'utf8');
    return fileContents;
  } catch (error) {
    // throw new Error(`Error reading file: ${error.message}`);
    return ""
  }
}

interface Result {
  Imagine: any; 
  Upscale: any;
}

async function main(): Promise<Result> {
  
  const client = new Midjourney({
    ServerId: <string>process.env.SERVER_ID,
    ChannelId: <string>process.env.CHANNEL_ID,
    SalaiToken: <string>process.env.SALAI_TOKEN,
    HuggingFaceToken: <string>process.env.HUGGINGFACE_TOKEN,
    Debug: false,
    Ws: true, // required  `Only you can see this`
  });

  await client.Connect(); // required
  
  const Imagine = await client.Imagine(
     String( readFileSync(filePath)),
    (uri: string, progress: string) => {
      // console.log("Imagine.loading", uri, "progress", progress);
    }
  );

  // console.log({ Imagine });
  if (!Imagine) {
    return { Imagine: null, Upscale: null };
  }

  const Upscale = await client.Upscale({
    index: 2,
    msgId: <string>Imagine.id,
    hash: <string>Imagine.hash,
    flags: Imagine.flags,
    loading: (uri: string, progress: string) => {
      // console.log("Upscale.loading", uri, "progress", progress);
    },
  });

  // console.log({ Upscale });

  client.Close();

  return { Imagine, Upscale };
}

main()
  .then((result: Result) => {
    // Tutaj możesz korzystać z wyniku, np. result.Imagine i result.Upscale
    console.log(result["Upscale"]["uri"]);
    // console.log("finished");
    // console.log(result);
    process.exit(0);
  })
  .catch((err) => {
    process.exit(1);
  });
