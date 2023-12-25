<script>
  let name = '';
  let description = '';
  let buyingPrice = '';
  let bidPrice = '';
  let photos = [];
  let photoURLs = [];
  const submitForm = () => {
    // Handle form submission here
  };
  $: if (photos && photos.length > 0) {
    photoURLs = Array.from(photos).map(photo => URL.createObjectURL(photo));
  }
</script>

<main>
  <h1>New Item</h1>
  <form on:submit|preventDefault={submitForm}>
    <label>
      Name of item:
      <input type="text" bind:value={name} required />
    </label>
    <label>
      Description:
      <textarea bind:value={description} required></textarea>
    </label>
    <label>
      Buying price:
      <input type="number" bind:value={buyingPrice} required />
    </label>
    <label>
      Bid price:
      <input type="number" bind:value={bidPrice} required />
    </label>
    <label> 
      Photo:
      <input type="file" bind:files={photos} accept="image/*" capture  multiple required />
    </label>
    <button type="submit">Submit</button>
  </form>
  {#each photoURLs as photoURL (photoURL)}
  <img src={photoURL} alt="Selected Photos" class="uploadPhoto"/>
  {/each}
</main>

<style>
  .uploadPhoto {
    width: 25vw;
    max-width: 100;
    height: auto;
    object-fit: contain;
  }
  
</style>
